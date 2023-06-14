#!/usr/bin/python3
'''1-write_file.py module'''


def write_file(filename="", text=""):
    '''
    A function that writes a string to a file

    Args:
        filename(str): Name of the file
        text(str): Text to write to file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
