import streamlit as st
from styles.css import MAIN_CSS
from components.chat import render_chat_section

st.set_page_config(layout="centered")

st.markdown(MAIN_CSS, unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

render_chat_section()