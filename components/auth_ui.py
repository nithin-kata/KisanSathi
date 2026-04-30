import streamlit as st
from components.auth_logic import login, signup

def render_auth_ui():

    st.markdown("""
    <style>

    /* ── BACKGROUND ── */
    .stApp {
        background: linear-gradient(135deg, #2E7D32, #66BB6A) !important;
    }

    .block-container {
        padding-top: 0rem !important;
    }

    /* ── CENTER CONTENT ── */
    .auth-container {
        max-width: 420px;
        margin: 120px auto;
        text-align: center;
    }

    /* ── TITLE ── */
    .app-title {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.3rem;
    }

    .app-subtitle {
        font-size: 0.9rem;
        color: rgba(255,255,255,0.85);
        margin-bottom: 2rem;
    }

    /* ── LABELS ── */
    label, .stTextInput label {
        color: white !important;
        font-weight: 500;
    }

    /* ── INPUTS ── */
    .stTextInput input {
        background: rgba(255,255,255,0.95) !important;
        color: black !important;
        border-radius: 10px !important;
        border: 1px solid rgba(0,0,0,0.2) !important;
        padding: 0.7rem !important;
    }

    .stTextInput input::placeholder {
        color: rgba(0,0,0,0.5) !important;
    }

    /* PASSWORD ICON */
    button[title="Show password text"] {
        color: black !important;
    }

    /* ── BUTTON ── */
    .stButton button {
        width: 100% !important;
        background: white !important;
        color: #2E7D32 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.7rem !important;
        margin-top: 12px;
    }

    /* ── RADIO ── */
    div.row-widget.stRadio > div {
        justify-content: center;
    }

    div.row-widget.stRadio label {
        color: white !important;
    }

    /* ── SUCCESS ALERT (FINAL FIX) ── */
    .stAlert {
        background: white !important;
        color: #2E7D32 !important;
        border-radius: 12px !important;
        padding: 0.9rem 1rem !important;
        margin-top: 14px !important;
        font-weight: 600;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }

    .stAlert svg {
        fill: #2E7D32 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ── UI ──
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)

    st.markdown("<div class='app-title'>🌱 KisanSathi</div>", unsafe_allow_html=True)
    st.markdown("<div class='app-subtitle'>Smart Farming Starts Here</div>", unsafe_allow_html=True)

    mode = st.radio("", ["Login", "Signup"], horizontal=True)

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Continue"):

        if mode == "Signup":
            if signup(username, password):
                st.success("Account created! Please login.")
            else:
                st.error("User already exists")

        else:
            if login(username, password):
                st.session_state["logged_in"] = True
                st.session_state["user"] = username
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.markdown("</div>", unsafe_allow_html=True)