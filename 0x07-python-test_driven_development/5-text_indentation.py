#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters ".", "?" and ":"

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    str = ""
    special_chars = (".", "?", ":")
    for char in text:
        str += char

        if char in special_chars:
            str += "\n\n"

    print(str)
