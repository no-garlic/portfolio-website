"""
Job History module for portfolio website.

This module contains the code to display the job history section of the portfolio,
showcasing professional experience and career trajectory.
"""

import streamlit as st
import json
import itertools
from utils import show_section


def show_games():
    show_portfolio("games.json")


def show_simulation():
    show_portfolio("simulation.json")


def show_portfolio(json_filename):
    """
    Display the job history section of the portfolio.    
    """
    with open(f"content/{json_filename}", "r") as file:
        data = json.load(file)

    main_title = data["title"]
    image_folder = data["image_folder"]

    with st.container(border=True):

        padding_left, content, padding_right = st.columns([0.025, 0.95, 0.025])
        with content:
            st.header(main_title)
            st.markdown("---")

        data_list = list(data["items"].items())
        
        # Create dictionaries for the left and right columns
        dict1 = dict(data_list[::2])
        dict2 = dict(data_list[1::2])

        # Create a 5-column layout with center-aligned main columns
        padding_left, column_left, padding_middle, column_right, padding_right = st.columns([0.025, 0.4, 0.05, 0.4, 0.025])

        # Render the two columns
        with column_left:
            show_section(dict1.items(), image_folder=image_folder)
        with column_right:
            show_section(dict2.items(), image_folder=image_folder)




"""
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
"""


