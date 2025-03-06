"""
Utility functions for the Streamlit application.

This script provides utility functions for loading images and markdown content,
which are used throughout the Streamlit app.
"""

import base64


def load_image(image_name: str, extension="jpeg") -> bytes:
    """
    Load an image and convert it to base64 format for use in HTML.
    :param image_name: Name of the image file (without extension)
    :param extension: Extension of the image file (default is jpeg)
    :return: Base64 encoded image content
    """
    with open(f"images/{image_name}.{extension}", "rb") as img_file:
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
