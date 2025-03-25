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

    for item in section:
        st.markdown(f"#### {item[1]["title"]}")

        details = f"- {item[1]["line1"]}"
        if "line2" in item[1]:
            details = f"{details}\n- {item[1]["line2"]}"
        if "line3" in item[1]:
            details = f"{details}\n- {item[1]["line3"]}"
        if "line4" in item[1]:
            details = f"{details}\n- {item[1]["line4"]}"
        if "line5" in item[1]:
            details = f"{details}\n- {item[1]["line5"]}"

        st.markdown(details)

        st.markdown(f" ")


def show_education():
    """
    Display the education section of the portfolio.
    
    Renders a header for the education section in the Streamlit app.
    """
    with open(f"content/education.json", "r") as file:
        data = json.load(file)

    main_title = data["main_title"]
    other_title = data["other_title"]

    with st.container(border=True):
        unused_1, col1, unused_2, col2, unused_3 = st.columns([0.05, 0.4, 0.1, 0.4, 0.05])

        with col1:
            st.markdown(f"## {main_title}")
            st.markdown("---")

            main = data["main"]
            show_section(main.items())

        with col2:
            st.markdown(f"## {other_title}")
            st.markdown("---")

            other = data["other"]
            show_section(other.items())
