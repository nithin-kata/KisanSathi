import streamlit as st
from styles.css import MAIN_CSS
from components.cost_calculator import render_cost_calculator

st.set_page_config(layout="centered")

# apply your theme
st.markdown(MAIN_CSS, unsafe_allow_html=True)

# page title (optional)
st.markdown("<div class='ks-section-label'>💰 Cost Calculator</div>", unsafe_allow_html=True)
st.markdown("<hr class='ks-divider'>", unsafe_allow_html=True)

# render feature
render_cost_calculator()