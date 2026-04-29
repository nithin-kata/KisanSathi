import streamlit as st
from styles.css import MAIN_CSS
from components.farmers import render_farmers_section

st.set_page_config(layout="centered")

st.markdown(MAIN_CSS, unsafe_allow_html=True)

render_farmers_section()