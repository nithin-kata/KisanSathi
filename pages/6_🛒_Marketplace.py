import streamlit as st
from components.marketplace import render_marketplace

st.set_page_config(layout="centered")

render_marketplace()