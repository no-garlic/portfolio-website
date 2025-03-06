"""
Projects module for portfolio website.

This module contains the code to display the projects section of the portfolio,
including project descriptions loaded from markdown files.
"""

import streamlit as st
import streamlit_antd_components as sac

from utils import load_markdown

# from portfolio_projects.pdf_search_rag_app.app import PdfSearchRagApp


def show_projects():
    """
    Display the projects section of the portfolio.
    
    Renders a header for the projects section and loads project content
    from a markdown file for display in the Streamlit app.
    """
    with st.container(border=False):
        #st.header("Projects")
        #st.markdown("---")

        tree_column, content_column = st.columns([1, 3])
        menu_index = 0

        with tree_column:
            with st.container(border=True):
                menu_index = sac.menu([
                    sac.MenuItem('AI Projects', icon='house-fill', children=[
                        sac.MenuItem('PDF Search', icon='file-pdf'),
                        sac.MenuItem('TODO', icon='alarm'),
                    ])
                ], indent=30, size='md', variant='filled', color="darkred", open_all=True, return_index=True)

        with content_column:
            with st.container(border=True):
                if menu_index == 0 or menu_index is None:
                    st.markdown("### Select a project from the menu")
                #elif menu_index == 1:
                #    PdfSearchRagApp().streamlit_main(subpage=True)
                else:
                    st.markdown("### Coming Soon...")
