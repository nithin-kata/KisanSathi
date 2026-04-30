import streamlit as st

# ── Page Config ─────────────────────────────────────────────
st.markdown("""
<h1 style='text-align:center;'>🌱 KisanSathi</h1>
<p style='text-align:center; color:gray;'>
AI-powered farming companion
</p>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.stTextInput input {
    border-radius: 12px;
}

.stButton button {
    border-radius: 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
}

.stButton button:hover {
    background-color: #3e8e41;
}
</style>
""", unsafe_allow_html=True)

# ── Imports ─────────────────────────────────────────────────
from components.chat import render_chat_section

# ❌ REMOVE THIS (causes heavy UI)
# from styles.css import MAIN_CSS
# st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Session State ───────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# ── Header ─────────────────────────────────────────────────
st.markdown("## 🌱 KisanSathi")
st.caption("Your AI-powered farming companion")

# ── CHAT ───────────────────────────────────────────────────
render_chat_section()

# ── Footer ─────────────────────────────────────────────────
st.markdown(
    """
    ---
    🌱 KisanSathi · Built for Indian Farmers  
    AI advice is suggestive — verify locally.
    """
)
