"""
Education module for portfolio website.

This module contains the code to display the education section of the portfolio,
showcasing academic background and educational achievements.
"""

import streamlit as st
from utils import load_markdown


def show_education():
    """
    Display the education section of the portfolio.
    
    Renders a header for the education section in the Streamlit app.
    """
    with st.container(border=True):
        st.header("Education")
        st.markdown("---")

        md = load_markdown("education")
        st.markdown(md)
