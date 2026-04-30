import streamlit as st

# simple in-memory storage (replace with DB later)
if "users" not in st.session_state:
    st.session_state["users"] = {}


def signup(username, password):
    if username in st.session_state["users"]:
        return False
    st.session_state["users"][username] = password
    return True


def login(username, password):
    return st.session_state["users"].get(username) == password