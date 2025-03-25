"""
Utility functions for the Streamlit application.

This script provides utility functions for loading images and markdown content,
which are used throughout the Streamlit app.
"""

import base64
from contextlib import contextmanager
import streamlit as st


HORIZONTAL_STYLE = """
<style class="hide-element">
    /* Hides the style container and removes the extra spacing */
    .element-container:has(.hide-element) {
        display: none;
    }
    /*
        The selector for >.element-container is necessary to avoid selecting the whole
        body of the streamlit app, which is also a stVerticalBlock.
    */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) {
        display: flex;
        flex-direction: row !important;
        flex-wrap: wrap;
        gap: 0.5rem;
        align-items: baseline;
    }
    /* Buttons and their parent container all have a width of 704px, which we need to override */
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) div {
        width: max-content !important;
    }
    /* Just an example of how you would style buttons, if desired */
    /*
    div[data-testid="stVerticalBlock"]:has(> .element-container .horizontal-marker) button {
        border-color: red;
    }
    */
</style>
"""


def load_image(image_name: str, path="", extension="jpeg") -> bytes:
    """
    Load an image and convert it to base64 format for use in HTML.
    :param image_name: Name of the image file (without extension)
    :param extension: Extension of the image file (default is jpeg)
    :return: Base64 encoded image content
    """
    with open(f"images/{path}{image_name}.{extension}", "rb") as img_file:
        content = base64.b64encode(img_file.read()).decode()
        return content


def load_markdown(content_name: str) -> str:
    """
    Load a markdown file and return its content as a string.
    :param content_name: Name of the markdown file (without extension)
    :return: Content of the markdown file
    """
    with open(f"content/{content_name}.md", "r") as f:
        content = f.read()
        return content


@contextmanager
def st_horizontal():
    st.markdown(HORIZONTAL_STYLE, unsafe_allow_html=True)
    with st.container():
        st.markdown('<span class="hide-element horizontal-marker"></span>', unsafe_allow_html=True)
        yield


@contextmanager
def st_sidebar_horizontal():
    st.sidebar.markdown(HORIZONTAL_STYLE, unsafe_allow_html=True)
    with st.sidebar.container():
        st.sidebar.markdown('<span class="hide-element horizontal-marker"></span>', unsafe_allow_html=True)
        yield


def st_image_link(image, link, width=100, gap=25, sidebar=False, align="center"):
    page_html=f"""
        <div style="display: flex; align-items: center; justify-content: {align}; gap: {gap}px;">
        <a href="{link}" target="_blank">
            <img src="data:image/png;base64,{image}" width="{width}">
        </a>
        </div>
        """
    if sidebar:
        st.sidebar.markdown(page_html, unsafe_allow_html=True)
    else:
        st.markdown(page_html, unsafe_allow_html=True)


