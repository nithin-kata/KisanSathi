"""
KisanSathi - Experts Component
Static expert cards with prefill-to-chat functionality
"""

import streamlit as st

# ── Static Expert Data ──
EXPERTS = [
    {
        "id": "soil",
        "emoji": "🧪",
        "name": "Dr. Ramesh Patel",
        "specialty": "Soil Scientist",
        "tag": "Soil & Nutrients",
        "experience": "18 yrs exp.",
        "prefill": "My soil is becoming hard and crops are not growing well. How can I improve soil health cheaply?",
    },
    {
        "id": "pest",
        "emoji": "🐛",
        "name": "Dr. Sunita Rao",
        "specialty": "Crop Protection Expert",
        "tag": "Pest & Disease",
        "experience": "14 yrs exp.",
        "prefill": "My crops have a pest attack. What are the best organic or low-cost ways to control pests?",
    },
    {
        "id": "water",
        "emoji": "💧",
        "name": "Mr. Anil Verma",
        "specialty": "Irrigation Specialist",
        "tag": "Water Management",
        "experience": "11 yrs exp.",
        "prefill": "How can I save water in irrigation? What are simple drip or sprinkler techniques for small farms?",
    },
]


def _render_expert_card(expert: dict, col):
    """Render a single expert card inside the given Streamlit column."""
    with col:
        st.markdown(
            f"""
            <div class='ks-expert-card'>
                <div class='ks-expert-avatar'>{expert['emoji']}</div>
                <div class='ks-expert-name'>{expert['name']}</div>
                <div class='ks-expert-specialty'>{expert['specialty']}</div>
                <div class='ks-expert-tag'>{expert['tag']}</div>
                <div style='font-size:0.75rem; color:var(--text-muted); margin-bottom:1rem;'>
                    ✅ {expert['experience']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Button outside HTML div for Streamlit event handling
        if st.button(f"Ask {expert['name'].split()[0]} →", key=f"expert_{expert['id']}"):
            st.session_state["prefill_query"] = expert["prefill"]
            st.rerun()


def render_experts_section():
    """Render the Experts section with cards in a column layout."""
    st.markdown("<div class='ks-section-label'>👨‍🔬 Our Agriculture Experts</div>", unsafe_allow_html=True)
    st.markdown("<hr class='ks-divider'>", unsafe_allow_html=True)

    cols = st.columns(len(EXPERTS), gap="medium")
    for expert, col in zip(EXPERTS, cols):
        _render_expert_card(expert, col)
