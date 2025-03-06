"""
AboutMe module for portfolio website.

This module contains the code to display the about me section of the portfolio,
providing personal information and background details.
"""

import streamlit as st
from utils import load_markdown

def show_aboutme():
    """
    Display the about me section of the portfolio.
    
    Renders a header for the about me section in the Streamlit app.
    """
    with st.container(border=True):
        md = load_markdown("about_me")
        st.markdown(md)
