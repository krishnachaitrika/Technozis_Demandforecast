import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Demand Forecast", page_icon="🎨", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: #e5e7eb;
}

.header {
    background: linear-gradient(90deg, #0b5ed7, #0a3cff);
    padding: 1.2rem 2rem;
    border-radius: 14px;
    margin-bottom: 1.2rem;
    color: white;
    font-weight: 700;
    font-size: 1.6rem;
}

.card {
    background: #0b1220;
    border: 1px solid #1f2933;
    border-radius: 14px;
    padding: 1.1rem 1.2rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
}

.metric-title { font-size: 0.75rem; color: #9ca3af; }
.metric-value { font-size: 1.3rem; font-weight: 700; color: #e5e7eb; }
.metric-sub   { font-size: 0.7rem;  color: #6b7280; }

.big-card {
    background: radial-gradient(circle at top right, #0b1220, #020617);
    border-radius: 18px;
    padding: 2rem;
    height: 100%;
    border: 1px solid #1f2933;
}

.price {
    font-size: 2.6rem;
    font-weight: 800;
    color: #22c55e;
    margin: 0.5rem 0;
}

.range {
    color: #9ca3af;
    font-size: 1.05rem;
}

.badge {
    display: inline-block;
    background: #052e16;
    color: #22c55e;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 0.75rem;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header with Indian Time ----------
ist = pytz.timezone("Asia/Kolkata")
now_ist = datetime.now(ist).strftime("%d %B %Y | %I:%M %p IST")

st.markdown(f"""
<div class="header">
Design Demand Forecast
<span style="float:right; font-size:0.85rem;">{now_ist} &nbsp; | &nbsp; Hyderabad, IN</span>
</div>
""", unsafe_allow_html=True)

# ---------- KPI Metrics ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1:
    st.markdown('<div class="card"><div class="metric-title">Market Demand</div><div class="metric-value">High</div><div class="metric-sub">+12% vs last month</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="card"><div class="metric-title">Avg. Material Cost</div><div class="metric-value">₹ 3,500 / sq.ft</div><div class="metric-sub">Stable trend</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="card"><div class="metric-title">Current Season</div><div class="metric-value">Peak</div><div class="metric-sub">Wedding & Renovation Season</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="card"><div class="metric-title">Crew Availability</div><div class="metric-value">85%</div><div class="metric-sub">12 teams active</div></div>', unsafe_allow_html=True)
with m5:
    st.markdown('<div class="card"><div class="metric-title">Active Leads</div><div class="metric-value">24</div><div class="metric-sub">8 high priority</div></div>', unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

# ---------- Main Section ----------
left, right = st.columns([2, 1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Input Variables")

    colA, colB = st.columns(2)
    with colA:
        project_scope = st.selectbox("Project Scope", [
            "Full Home Renovation", "Kitchen Remodel", "Bedroom Upgrade", "Living Room Design"
        ])
        square_ft = st.slider("Square Footage", 500, 5000, 1500, step=50)

    with colB:
        design_style = st.selectbox("Design Style", [
            "Modern Minimalist", "Contemporary", "Luxury", "Traditional"
        ])
        material_grade = st.select_slider("Material Grade", options=["Standard", "Premium", "Luxury"], value="Premium")

    urgency = st.radio("Project Urgency", ["Low", "Medium", "High"], horizontal=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="big-card">', unsafe_allow_html=True)
    st.subheader("Recommended Price Range")

    # Dummy price logic in INR (replace with ML later)
    base_price = 2_50_000 + (square_ft * 120)  # base interior cost logic (₹)
    if material_grade == "Premium":
        base_price *= 1.2
    elif material_grade == "Luxury":
        base_price *= 1.5

    low = int(base_price * 0.95)
    high = int(base_price * 1.08)

    st.markdown(f'<div class="price">₹ {low:,.0f}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="range">to ₹ {high:,.0f}</div>', unsafe_allow_html=True)

    margin = "22%" if material_grade == "Premium" else "18%" if material_grade == "Standard" else "28%"
    st.markdown(f'<div class="badge">Estimated Profit Margin: {margin}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
