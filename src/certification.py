"""
Certification module for portfolio website.

This module contains the code to display the certification section of the portfolio,
using Streamlit Antd Components for interactive visualization of certifications.
"""

import streamlit as st
import json
import itertools
from utils import load_image, st_image_link, st_horizontal


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

        show_separator = False
        iterator = iter(data["items"].items())

        for pair in itertools.zip_longest(iterator, iterator, fillvalue=None):
            unused_1, col1, unused_2, col2, unused_3 = st.columns([0.05, 0.4, 0.1, 0.4, 0.05])

            key_1 = pair[0][0]
            val_1 = pair[0][1]
            key_2 = pair[1][0]
            val_2 = pair[1][1]
                        
            with col1:
                if show_separator:
                    st.markdown("---")
                st.markdown(f"## {val_1['org']}")
                st.markdown(f"### {val_1['title']}")
                
                img = load_image(key_1, image_folder, extension="jpg")
                st_image_link(img, link=val_1["certificate_link"], width=image_width, align="left")
                
            with col2:
                if show_separator:
                    st.markdown("---")
                st.markdown(f"## {val_2['org']}")
                st.markdown(f"### {val_2['title']}")

                img = load_image(key_2, image_folder, extension="jpg")
                st_image_link(img, link=val_2["certificate_link"], width=image_width, align="left")

            st.markdown("###### ")
            show_separator = True

