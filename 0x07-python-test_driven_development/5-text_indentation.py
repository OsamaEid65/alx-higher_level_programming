#!/usr/bin/python3
def text_indentation(text):
    """method to print text and print 2 lines
    Args:
         text:the input
    Raises:
        raise a TypeError if the input was not str
    """
    special_chars = ["?", ".", ":"]
    if any(c in text for c in special_chars):
        new_text = text
        for c in special_chars:
            new_text = new_text.replace(c, c + "\n\n")
        print(new_text + "\n")
    else:
        print(text + "\n")
