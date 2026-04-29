import streamlit as st
import uuid

def render_cost_calculator():

    st.markdown("## 💰 Farm Expense Calculator")

    # ── Initialize ──
    if "cost_items" not in st.session_state:
        st.session_state["cost_items"] = []

    # ── Add new expense ──
    st.markdown("### ➕ Add Expense")

    col1, col2, col3 = st.columns([2,2,1])

    with col1:
        name = st.text_input("Expense Name", placeholder="e.g. Tractor Rent")

    with col2:
        category = st.selectbox(
            "Category",
            ["Labor", "Equipment", "Input", "Transport", "Other"],
            key="category_select"
        )

    with col3:
        if st.button("Add"):
            if name.strip():
                st.session_state["cost_items"].append({
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "category": category,
                    "value": 0
                })
                st.rerun()

    st.markdown("---")

    total = 0

    # ── Show all expenses ──
    if st.session_state["cost_items"]:
        st.markdown("### 📋 Expenses")

    for item in st.session_state["cost_items"]:

        col1, col2, col3, col4 = st.columns([2,2,2,1])

        with col1:
            st.write(f"**{item['name']}**")

        with col2:
            st.caption(item["category"])

        with col3:
            value = st.number_input(
                "₹",
                min_value=0,
                value=item["value"],
                key=f"value_{item['id']}",
                label_visibility="collapsed"
            )
            item["value"] = value

        with col4:
            if st.button("❌", key=f"remove_{item['id']}"):
                st.session_state["cost_items"] = [
                    i for i in st.session_state["cost_items"]
                    if i["id"] != item["id"]
                ]
                st.rerun()

        total += value

    st.markdown("---")

    # ── Total ──
    st.success(f"💰 Total Investment: ₹ {total}")