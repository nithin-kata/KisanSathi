import streamlit as st
from components.auth_ui import render_auth_ui

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

if not st.session_state.get("logged_in"):
    render_auth_ui()
    st.stop()
from components.header import render_header
from components.chat import render_chat_section

from styles.css import MAIN_CSS

st.markdown(MAIN_CSS, unsafe_allow_html=True)
# ── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="KisanSathi 🌱",
    layout="wide"
)

# ── Global CSS ──────────────────────────────────────────────
st.markdown("""
<style>

/* Full-width layout */
.block-container {
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
    padding-top: 1rem;
}

/* Full-width banner fix */
.ks-banner {
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    border-radius: 0px !important;
}

/* Buttons */
.stButton button {
    border-radius: 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
}
.stButton button:hover {
    background-color: #3e8e41;
}

/* Inputs */
.stTextInput input {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ── Session State ───────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# ── ONLY HEADER (your banner) ───────────────────────────────
render_header()

# ── CHAT ───────────────────────────────────────────────────
render_chat_section()

# ── Footer ─────────────────────────────────────────────────
st.markdown("""
---
🌱 KisanSathi · Built for Indian Farmers  
AI advice is suggestive — verify locally.
""")
