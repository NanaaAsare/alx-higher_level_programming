#!/usr/bin/python3
'''2-append_write.py module'''


def append_write(filename="", text=""):
    '''
    A function that appends a text to a file.

    Args:
        filename(str): name of the file
        text(str): text to append to file
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
