#!/usr/bin/python3
'''6-load_from_json_file.py module'''


import json


def load_from_json_file(filename):
    '''
    A function to load the contents of a JSON file

    Args:
        filename(str): name of the file
    '''

    with open(filename, 'r') as f:
        return json.load(f)
