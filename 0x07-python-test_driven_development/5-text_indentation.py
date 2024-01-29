#!/usr/bin/python3

"""This function fines a text-indentation function."""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    mc = 0
    while mc < len(text) and text[mc] == ' ':
        mc += 1

    while mc < len(text):
        print(text[mc], end="")
        if text[mc] == "\n" or text[mc] in ".?:":
            if text[mc] in ".?:":
                print("\n")
            mc += 1
            while mc < len(text) and text[mc] == ' ':
                mc += 1
            continue
        mc += 1
