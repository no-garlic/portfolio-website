"""
Blog module for portfolio website.

This module contains the code to display the blog section of the portfolio,
showcasing articles, posts, and other written content.
"""

import streamlit as st
import streamlit_antd_components as sac

from utils import load_markdown


def show_blog():
    """
    Display the blog section of the portfolio.
    
    Renders a header for the blog section in the Streamlit app.
    """
    with st.container(border=True):
        st.header("Blog")
        st.markdown("---")
