import streamlit as st
from styles.css import MAIN_CSS
from components.crop_planner import render_crop_planner

st.set_page_config(layout="centered")

st.markdown(MAIN_CSS, unsafe_allow_html=True)

render_crop_planner()