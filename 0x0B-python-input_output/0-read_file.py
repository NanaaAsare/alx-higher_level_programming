#!/usr/bin/python3
'''0-read_file module'''


def read_file(filename=""):
    '''
    A function that reads a file and prints it to
    stdout.

    Args:
        filename(str): The name of the file
    '''

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
