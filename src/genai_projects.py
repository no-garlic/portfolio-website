"""
Projects module for portfolio website.

This module contains the code to display the projects section of the portfolio,
including project descriptions loaded from markdown files.
"""

import streamlit as st
import json
import itertools


def show_genai_projects():
    """
    Display the projects section of the portfolio.
    
    Renders a header for the projects section and loads project content
    from a markdown file for display in the Streamlit app.
    """
    with open(f"content/genai_projects.json", "r") as file:
        data = json.load(file)


    if "genai_project" in st.session_state:
        current_project = st.session_state["genai_project"]
        if current_project is not None:
            st.markdown(f"### Current Project: {current_project}")

    page_title = data["title"]
    image_folder = data["image_folder"]
    image_width = int(data["image_width"])
    
    with st.container(border=True):
        padding_left, content, padding_right = st.columns([0.025, 0.95, 0.025])
        with content:
            st.header(page_title)
            st.markdown("---")

        index = 0
        iterator = iter(data["items"].items())
        for pair in itertools.zip_longest(iterator, iterator, iterator, fillvalue=None):
            columns = st.columns([0.025, 0.3, 0.35, 0.3, 0.025])

            for i in range(3):
                with columns[i + 1]:
                    if pair[i]:
                        key = pair[i][0]
                        val = pair[i][1]
                        st.markdown(f"### {val['title']}")
                        st.image(f"{image_folder}/{key}.jpg", width=image_width)
                        if st.button("Launch Project", key=index):
                            st.session_state["genai_project"] = val["title"]

                        index = index + 1

            st.markdown("###### ")


