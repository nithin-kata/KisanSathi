import streamlit as st

# ── Page Config ─────────────────────────────────────────────

st.set_page_config(
page_title="KisanSathi 🌱",
page_icon="🌱",
layout="centered",
initial_sidebar_state="expanded",
)

# ── Imports ─────────────────────────────────────────────────

from styles.css import MAIN_CSS
from components.chat import render_chat_section

# ── Apply CSS ───────────────────────────────────────────────

st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Session State ───────────────────────────────────────────

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# ── Header ─────────────────────────────────────────────────

st.markdown(
""" <div class="ks-header"> <div class="ks-header-title">🌱 KisanSathi</div> <div class="ks-header-tagline">
Your AI-powered farming companion </div> </div>
""",
unsafe_allow_html=True,
)

# ── CHAT ON HOME PAGE ───────────────────────────────────────

render_chat_section()

# ── Footer ─────────────────────────────────────────────────

st.markdown(
""" <div class="ks-footer">
🌱 KisanSathi · Built with ❤️ for Indian Farmers ·
AI advice is suggestive — verify with local experts. </div>
""",
unsafe_allow_html=True,
)
