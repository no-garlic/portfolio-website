"""
Sidebar module for the Streamlit application.

This script defines the sidebar navigation for the Streamlit app, including
loading and displaying the user's image and providing navigation options
to different sections of the portfolio.
"""

import streamlit as st
from streamlit_option_menu import option_menu

from aboutme import show_aboutme
from certification import show_certification
from education import show_education
from portfolio import show_simulation, show_games
from projects import show_projects
from blog import show_blog

from utils import load_image


def show_sidebar():
    """
    Show the sidebar with navigation options.
    :return: The show_xxx function of the selected page.
    """

    # load the image of mike
    mike_img = load_image("mike")

    # create a style where the image is masked out under a circle
    mike_img_html = f"""
        <style>
        .logo-container {{
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }}
        .logo {{
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
        }}
        </style>
        <div class="logo-container">
            <img src="data:image/png;base64,{mike_img}" class="logo">
        </div>
    """

    # draw the image in the sidebar
    st.sidebar.markdown(mike_img_html, unsafe_allow_html=True)

    # create the dictionary of navigation menu names and show_xxx functions
    nav_funcs = {
        "About me": show_aboutme,
        "Projects": show_projects,
        "Certification": show_certification,
        "Game Development": show_games,
        "Simulator Development": show_simulation,
        "Education": show_education,
        "Blog": show_blog
    }

    # create the sidebar with the navigation menu
    with st.sidebar:
        pages = list(nav_funcs.keys())
        nav_tab_op = option_menu(
            menu_title="Michael Petrou",
            options=pages,
            icons=['person-fill', 'files', 'file-text', 'controller', 'airplane-engines', 'mortarboard', 'pencil'], # spare: 'person-square'
            menu_icon="file-earmark-text",
            default_index=0,
            styles={"nav-link": {"margin":"4px", "--hover-color": "#c99"}}
        )

    # return the show_xxx function for the selected page
    for key, value in nav_funcs.items():
        if nav_tab_op == key:
            return value
        
    # if no page is selected, then return None
    return None
