"""
KisanSathi - Nearby Farmers Component
Static list of nearby farmers with prefill-to-chat functionality
"""

import streamlit as st

# ── Static Farmer Data ──
FARMERS = [
    {
        "id": "ramesh",
        "emoji": "👨‍🌾",
        "name": "Ramesh Kumar",
        "distance": "1.2 km away",
        "crop": "🌾 Wheat",
        "village": "Pratappur Village",
        "prefill": "I want to connect with a nearby wheat farmer. I have questions about wheat cultivation techniques and when to harvest.",
    },
    {
        "id": "priya",
        "emoji": "👩‍🌾",
        "name": "Priya Devi",
        "distance": "2.8 km away",
        "crop": "🍅 Tomato",
        "village": "Nandanpur Village",
        "prefill": "I want to learn about tomato farming from a local farmer. What are the best practices for growing tomatoes in this region?",
    },
    {
        "id": "mohan",
        "emoji": "👨‍🌾",
        "name": "Mohan Singh",
        "distance": "4.5 km away",
        "crop": "🌽 Maize",
        "village": "Kishanpur Village",
        "prefill": "I am interested in maize farming. What are the common problems in maize crops and how to solve them affordably?",
    },
    {
        "id": "sunita",
        "emoji": "👩‍🌾",
        "name": "Sunita Yadav",
        "distance": "6.1 km away",
        "crop": "🧅 Onion",
        "village": "Rampur Colony",
        "prefill": "I want to know about onion farming. When is the best time to plant onions and how to store them after harvest?",
    },
]


def _render_farmer_row(farmer: dict):
    """Render a single farmer row card with chat button."""
    col_info, col_btn = st.columns([4, 1])

    with col_info:
        st.markdown(
            f"""
            <div class='ks-farmer-row'>
                <div class='ks-farmer-icon'>{farmer['emoji']}</div>
                <div class='ks-farmer-info'>
                    <div class='ks-farmer-name'>{farmer['name']}</div>
                    <div class='ks-farmer-meta'>
                        📍 {farmer['distance']} &nbsp;·&nbsp; {farmer['village']}
                        <span class='ks-farmer-crop'>{farmer['crop']}</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_btn:
        # Vertically center the button
        st.markdown("<div style='padding-top:0.6rem;'>", unsafe_allow_html=True)
        if st.button("💬 Chat", key=f"farmer_{farmer['id']}"):
            st.session_state["prefill_query"] = farmer["prefill"]
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


def render_farmers_section():
    """Render the Nearby Farmers section as a list of cards."""
    st.markdown("<div class='ks-section-label'>🚜 Nearby Farmers</div>", unsafe_allow_html=True)
    st.markdown("<hr class='ks-divider'>", unsafe_allow_html=True)

    for farmer in FARMERS:
        _render_farmer_row(farmer)
