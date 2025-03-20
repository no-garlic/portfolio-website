"""
Certification module for portfolio website.

This module contains the code to display the certification section of the portfolio,
using Streamlit Antd Components for interactive visualization of certifications.
"""

import streamlit as st
import json
import itertools


def show_certification():
    """
    Display the certification section of the portfolio.
    
    Renders a header for the certification section and creates a two-column layout
    with navigation menu in the left column and content in the right column.
    """
    with open(f"content/certification.json", "r") as file:
        data = json.load(file)

    page_title = data["title"]
    image_folder = data["image_folder"]
    image_width = int(data["image_width"])
    
    with st.container(border=True):
        st.header(page_title)
        st.markdown("---")

        iterator = iter(data["items"].items())

        for pair in itertools.zip_longest(iterator, iterator, fillvalue=None):
            unused_1, col1, col2, unused_2 = st.columns([0.05, 0.45, 0.45, 0.05])

            key_1 = pair[0][0]
            val_1 = pair[0][1]
            key_2 = pair[1][0]
            val_2 = pair[1][1]
            
            with col1:
                st.markdown(f"### {val_1['title']}")
                st.image(f"{image_folder}/{key_1}.jpg", width=image_width)
                
            with col2:
                st.markdown(f"### {val_2['title']}")
                st.image(f"{image_folder}/{key_2}.jpg", width=image_width)

            st.markdown("###### ")



