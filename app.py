"""
KisanSathi 🌱 — AI Agriculture Assistant for Indian Farmers
Entry point: streamlit run app.py

Architecture:
    app.py                  ← orchestrator & layout
    components/
        chat.py             ← AI chat UI + Groq integration
        experts.py          ← Expert cards
        farmers.py          ← Nearby farmers list
    utils/
        groq_client.py      ← Groq API wrapper
    styles/
        css.py              ← All custom CSS
"""

import streamlit as st

st.set_page_config(
    page_title="KisanSathi 🌱 — Your Farming AI Companion",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="expanded",
)

from styles.css import MAIN_CSS
from components.chat import render_chat_section
from components.experts import render_experts_section
from components.farmers import render_farmers_section

# ── Inject CSS ────────────────────────────────────────────────────────────────
st.markdown(MAIN_CSS, unsafe_allow_html=True)


# ── Session State Init ────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


# ── Header ────────────────────────────────────────────────────────────────────
# ── Home Page Only ─────────────────────────────────────────

st.markdown(
    """
    <div class="ks-header">
        <div class="ks-header-title">🌱 KisanSathi</div>
        <div class="ks-header-tagline">
            Your AI-powered farming companion
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### 👋 Welcome")
st.markdown("""
Use the sidebar to navigate:

- 💬 Chat with AI  
- 👨‍🌾 Experts  
- 📍 Nearby Farmers  
""")
# ── Experts Section ───────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)


# ── Nearby Farmers Section ────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)


# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="ks-footer">
        🌱 KisanSathi &nbsp;·&nbsp; Built with ❤️ for Indian Farmers &nbsp;·&nbsp;
        Advice is AI-generated — always consult a local agronomist for critical decisions.
    </div>
    """,
    unsafe_allow_html=True,
)
