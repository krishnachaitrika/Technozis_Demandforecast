import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("interior_data.csv")
encoders = {}
for col in ["house_type", "city_type", "style", "package"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features & target
X = df[["house_type", "area_sqft", "rooms", "city_type", "budget_lakhs", "style", "package"]]
y = df["cost_lakhs"]

# Train model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X, y)

# Save model 
joblib.dump(model, "model.pkl")
joblib.dump(encoders, "encoders.pkl")

print("✅ Model trained and saved!")
