import streamlit as st
from utils.groq_client import get_ai_response

# basic mapping
CROP_DATA = {
    "Punjab": ["Wheat", "Rice"],
    "Maharashtra": ["Cotton", "Soybean"],
    "Andhra Pradesh": ["Rice", "Chilli"],
    "Telangana": ["Maize", "Cotton"]
}

CROP_INFO = {
    "Wheat": {"yield": 20, "price": 2200, "cost": 15000, "season": "Nov-Apr"},
    "Rice": {"yield": 25, "price": 2000, "cost": 18000, "season": "Jun-Oct"},
    "Cotton": {"yield": 10, "price": 6000, "cost": 20000, "season": "May-Oct"},
    "Soybean": {"yield": 12, "price": 4000, "cost": 12000, "season": "Jun-Sep"},
    "Maize": {"yield": 18, "price": 1800, "cost": 14000, "season": "Jul-Nov"},
    "Chilli": {"yield": 8, "price": 7000, "cost": 25000, "season": "Jun-Dec"},
}


def calculate_profit(crop, land):
    d = CROP_INFO[crop]
    revenue = d["yield"] * d["price"] * land
    cost = d["cost"] * land
    profit = revenue - cost
    return profit, d["season"]


def render_crop_planner():

    st.markdown("## 🌱 AI Crop Planner")

    land = st.number_input("Land Size (acres)", min_value=0.5, step=0.5)

    location = st.selectbox("Location", list(CROP_DATA.keys()))

    if st.button("Generate Plan"):

        crops = CROP_DATA.get(location, [])

        plans = []
        st.subheader("📊 Options")

        for crop in crops:
            profit, season = calculate_profit(crop, land)

            plans.append({"crop": crop, "profit": profit, "season": season})

            st.write(f"🌾 {crop} → ₹{profit} profit | {season}")

        # AI explanation
        prompt = f"""
        Suggest best crop for:
        Land: {land} acres
        Location: {location}
        Options: {plans}

        Give best crop, reason, timeline, tips.
        """

        with st.spinner("AI thinking..."):
            response = get_ai_response(prompt)

        st.subheader("🤖 Recommendation")
        st.write(response)