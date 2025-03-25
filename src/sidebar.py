"""
Sidebar module for the Streamlit application.

This script defines the sidebar navigation for the Streamlit app, including
loading and displaying the user's image and providing navigation options
to different sections of the portfolio.
"""

import streamlit as st
from streamlit_option_menu import option_menu
from social_media import SocialMediaIcons
from utils import load_image, st_sidebar_horizontal

from aboutme import show_aboutme
from certification import show_certification
from portfolio import show_simulation, show_games
from education import show_education
from jobs import show_jobs
#from genai_projects import show_genai_projects
#from blog import show_blog


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
        "About Me": show_aboutme,
        "Certification": show_certification,
        "Game Development": show_games,
        "Simulator Development": show_simulation,
        "Education": show_education,
        "Jobs": show_education,
#        "Gen AI Projects": show_genai_projects,
#        "Blog": show_blog
    }

    nav_icons=[
        'person-fill',
        'file-text', 
        'controller', 
        'airplane-engines', 
        'award-fill',
        'calendar-plus',
#        'files', 
#        'pencil',
#        'person-square'
#        'mortarboard', 
    ]

    # create the sidebar menu for the page navigation
    with st.sidebar:
        pages = list(nav_funcs.keys())
        nav_tab_op = option_menu(
            menu_title="Michael Petrou",
            options=pages,
            icons=nav_icons,
            menu_icon="file-earmark-text",
            default_index=0,
            styles={"nav-link": {"margin":"4px", "--hover-color": "#c99"}}
        )

    # create the sidebar menu for the projects
    if nav_tab_op == "Gen AI Projects":
        with st.sidebar:
            pages = list(("a", "b"))
            nav_tab_project = option_menu(
                menu_title="Gen AI Projects",
                options=pages,
                #icons=nav_icons,
                menu_icon="file-earmark-text",
                default_index=0,
                styles={"nav-link": {"margin":"4px", "--hover-color": "#c99"}}
            )
        st.session_state["genai_project"] = nav_tab_project


    # show the social media links
    with st.sidebar:
        social_media_links = [
            "https://github.com/no-garlic", 
            "https://www.linkedin.com/in/mpetrou"
        ]        
        social_media_colors = [
            "#BBBBBB", 
            "#0A66C2"
        ]
        social_media_icons = SocialMediaIcons(social_media_links, colors=social_media_colors, size=50, gap=25)
        social_media_icons.render()


    # return the show_xxx function for the selected page
    for key, value in nav_funcs.items():
        if nav_tab_op == key:
            return value
        
    # if no page is selected, then return None
    return None
