"""
Job History module for portfolio website.

This module contains the code to display the job history section of the portfolio,
showcasing professional experience and career trajectory.
"""

import streamlit as st


def show_jobhistory():
    """
    Display the job history section of the portfolio.
    
    Renders a header for the job history section in the Streamlit app.
    """
    with st.container(border=True):
        st.header("Job History")
        st.markdown("---")
