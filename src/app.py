"""
Main entry point for the Streamlit application.

This script sets up the Streamlit app, including the page configuration,
sidebar navigation, and footer.
"""

import streamlit as st

from sidebar import show_sidebar
from headerfooter import footer

# set the page title and layout
st.set_page_config(page_title="Michael Petrou - Portfolio", layout="wide", initial_sidebar_state="expanded", page_icon="💻")

# show the sidebar and determine which page is selected
selected_page = show_sidebar()

# if there is a selected page, then call the show function for that page
if selected_page != None:
    selected_page()

# draw the page footer
st.markdown(footer, unsafe_allow_html=True)
