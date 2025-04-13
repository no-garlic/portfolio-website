"""
Education module for portfolio website.

This module contains the code to display the education section of the portfolio,
showcasing academic background and educational achievements.
"""

import streamlit as st
import json
from utils import show_section


def show_work_history():
    """
    Display the education section of the portfolio.
    
    Renders a header for the education section in the Streamlit app.
    """
    # Load education data from JSON file
    with open(f"content/work_history.json", "r") as file:
        data = json.load(file)

    # Extract main and section titles
    main_title = data["main_title"]
    other_title = data["other_title"]

    # Create a container with a border
    with st.container(border=True):
        # Create a 5-column layout with center-aligned main columns
        padding_left, column_left, padding_middle, column_right, padding_right = st.columns([0.025, 0.4, 0.05, 0.4, 0.025])

        # Render main education column
        with column_left:
            st.markdown(f"## {main_title}")
            st.markdown("---")

            main = data["main"]
            show_section(main.items())

        # Render other education column
        with column_right:
            st.markdown(f"## {other_title}")
            st.markdown("---")

            other = data["other"]
            show_section(other.items())