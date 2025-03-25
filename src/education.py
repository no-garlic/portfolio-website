"""
Education module for portfolio website.

This module contains the code to display the education section of the portfolio,
showcasing academic background and educational achievements.
"""

import streamlit as st
import json
import itertools
from utils import load_markdown


def show_section(section):
    """
    Render a section of education or experience items in Streamlit.
    
    Args:
        section (dict or iterable): A collection of items to be displayed.
    """
    for _, item in section:
        # Render the title
        st.markdown(f"#### {item['title']}")
        
        # Collect detail lines
        details = []
        line_number = 1
        while f'line{line_number}' in item:
            details.append(item[f'line{line_number}'])
            line_number += 1
        
        # Render details as a markdown list if there are any
        if details:
            formatted_details = "\n".join(f"- {line}" for line in details)
            st.markdown(formatted_details)
        
        # Add a small separator
        st.markdown(" ")


def show_education():
    """
    Display the education section of the portfolio.
    
    This function performs the following tasks:
    1. Loads education data from a JSON file located at 'content/education.json'
    2. Creates a two-column layout to display main and other educational experiences
    3. Renders section titles and details using the show_section() function
    
    The function expects a specific JSON structure with the following keys:
    - main_title: Title for the primary education column
    - other_title: Title for the secondary education column
    - main: Dictionary of primary educational experiences
    - other: Dictionary of secondary/additional educational experiences
    
    Layout:
    - Uses a 5-column grid with center-aligned 2 main columns
    - Left column displays main educational experiences
    - Right column displays other educational experiences
    
    Raises:
    - FileNotFoundError: If the education.json file cannot be found
    - JSONDecodeError: If the JSON file is improperly formatted
    """
    # Load education data from JSON file
    with open(f"content/education.json", "r") as file:
        data = json.load(file)

    # Extract main and section titles
    main_title = data["main_title"]
    other_title = data["other_title"]

    # Create a container with a border
    with st.container(border=True):
        # Create a 5-column layout with center-aligned main columns
        unused_1, col1, unused_2, col2, unused_3 = st.columns([0.05, 0.4, 0.1, 0.4, 0.05])

        # Render main education column
        with col1:
            st.markdown(f"## {main_title}")
            st.markdown("---")

            main = data["main"]
            show_section(main.items())

        # Render other education column
        with col2:
            st.markdown(f"## {other_title}")
            st.markdown("---")

            other = data["other"]
            show_section(other.items())
