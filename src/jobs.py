"""
Education module for portfolio website.

This module contains the code to display the education section of the portfolio,
showcasing academic background and educational achievements.
"""

import streamlit as st
from utils import load_markdown


def show_jobs():
    """
    Display the education section of the portfolio.
    
    Renders a header for the education section in the Streamlit app.
    """
    with st.container(border=True):
        st.header("Work History")
        st.markdown("---")

        md = load_markdown("work_history")
        st.markdown(md)
