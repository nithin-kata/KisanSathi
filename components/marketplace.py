import streamlit as st
import uuid

def render_marketplace():

    st.markdown("## 🛒 Farmer Marketplace")

    # ── Init DB (in-memory) ──
    if "listings" not in st.session_state:
        st.session_state["listings"] = []

    if "farmer_name" not in st.session_state:
        st.session_state["farmer_name"] = ""

    # ── Role Selection ──
    role = st.radio("I am a:", ["Farmer 👨‍🌾", "Buyer 🛒"], horizontal=True)

    st.markdown("---")

    # =========================================================
    # 👨‍🌾 FARMER SECTION
    # =========================================================
    if role == "Farmer 👨‍🌾":

        st.subheader("📦 List Your Crop")

        name = st.text_input("Farmer Name", value=st.session_state["farmer_name"])
        crop = st.text_input("Crop (e.g. Wheat)")
        quantity = st.number_input("Quantity (quintals)", min_value=1)
        price = st.number_input("Price per quintal (₹)", min_value=1)
        location = st.text_input("Location")

        # Save farmer name in session
        if name:
            st.session_state["farmer_name"] = name

        if st.button("📤 Add Listing"):
            if name and crop and location:

                st.session_state["listings"].append({
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "crop": crop,
                    "quantity": quantity,
                    "price": price,
                    "location": location
                })

                st.success("Listing added successfully!")
                st.rerun()

        st.markdown("---")

        # ── Farmer Listings ──
        st.subheader("📋 My Listings")

        has_listings = False

        for item in st.session_state["listings"]:

            if item["name"] != st.session_state["farmer_name"]:
                continue

            has_listings = True

            st.markdown(f"""
            **🌾 {item['crop']}**
            - Quantity: {item['quantity']} quintals
            - Price: ₹{item['price']} / quintal
            - Location: {item['location']}
            """)

            if st.button("❌ Delist", key=f"delist_{item['id']}"):
                st.session_state["listings"] = [
                    i for i in st.session_state["listings"]
                    if i["id"] != item["id"]
                ]
                st.success("Listing removed")
                st.rerun()

        if not has_listings:
            st.info("No listings yet. Add your first crop above.")

    # =========================================================
    # 🛒 BUYER SECTION
    # =========================================================
    else:

        st.subheader("🔍 Available Crops")

        crop_filter = st.text_input("Filter by crop")
        location_filter = st.text_input("Filter by location")

        found = False

        for item in st.session_state["listings"]:

            if crop_filter and crop_filter.lower() not in item["crop"].lower():
                continue

            if location_filter and location_filter.lower() not in item["location"].lower():
                continue

            found = True

            st.markdown(f"""
            **🌾 {item['crop']}**
            - Farmer: {item['name']}
            - Quantity: {item['quantity']} quintals
            - Price: ₹{item['price']} / quintal
            - Location: {item['location']}
            """)

            if st.button("📞 Contact Farmer", key=f"contact_{item['id']}"):
                st.info(f"Contact {item['name']} (demo feature)")

        if not found:
            st.warning("No matching listings found.")