"""
Certification module for portfolio website.

This module contains the code to display the certification section of the portfolio,
using Streamlit Antd Components for interactive visualization of certifications.
"""

import streamlit as st


def show_certification():
    """
    Display the certification section of the portfolio.
    
    Renders a header for the certification section and creates a two-column layout
    with navigation menu in the left column and content in the right column.
    """
    with st.container(border=True):
        st.header("Certification")
        st.markdown("---")

