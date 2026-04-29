import streamlit as st
from styles.css import MAIN_CSS
from components.experts import render_experts_section

st.set_page_config(layout="centered")

st.markdown(MAIN_CSS, unsafe_allow_html=True)

render_experts_section()