import streamlit as st
from utilities import build_page_navigation

# Set the page configuration
st.set_page_config(
    page_title="Michael Wilt",
    layout="wide",
    initial_sidebar_state="collapsed",
)

build_page_navigation()
