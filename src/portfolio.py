"""
Job History module for portfolio website.

This module contains the code to display the job history section of the portfolio,
showcasing professional experience and career trajectory.
"""

import streamlit as st
import json
import itertools


def show_games():
    show_portfolio("games.json")

def show_simulation():
    show_portfolio("simulation.json")

def show_portfolio(json_filename):
    """
    Display the job history section of the portfolio.
    
    Renders a header for the job history section in the Streamlit app.
    """
    with open(f"content/{json_filename}", "r") as file:
        data = json.load(file)

    page_title = data["title"]
    image_folder = data["image_folder"]

    with st.container(border=True):
        st.header(page_title)
        st.markdown("---")

        iterator = iter(data["items"].items())

        for pair in itertools.zip_longest(iterator, iterator, fillvalue=None):
            unused_1, col1, col2, col3, col4, unused_2 = st.columns([0.05, 0.075, 0.375, 0.075, 0.375, 0.05])

            key_1 = pair[0][0]
            val_1 = pair[0][1]
            key_2 = pair[1][0]
            val_2 = pair[1][1]
            
            with col1:
                st.image(f"{image_folder}/{key_1}.jpg", width=150)
            with col2:
                st.markdown(f"##### {val_1['title']}")

                bullets = f"- {val_1['line1']}"
                if "line2" in val_1:
                    bullets = f"{bullets}\n - {val_1['line2']}"
                if "line3" in val_1:
                    bullets = f"{bullets}\n - {val_1['line3']}"

                st.markdown(bullets)
                
            with col3:
                st.image(f"{image_folder}/{key_2}.jpg", width=150)
            with col4:
                st.markdown(f"##### {val_2['title']}")

                bullets = f"- {val_2['line1']}"
                if "line2" in val_2:
                    bullets = f"{bullets}\n - {val_2['line2']}"
                if "line3" in val_2:
                    bullets = f"{bullets}\n - {val_2['line3']}"

                st.markdown(bullets)

            st.markdown("###### ")



