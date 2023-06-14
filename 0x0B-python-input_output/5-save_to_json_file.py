#!/usr/bin/python3
'''5-save_to_json_file.py module'''


import json


def save_to_json_file(my_obj, filename):
    '''
    A function that writes a python object to
    a file using JSON representation.

    Args:
        my_obj(object): object to save in file
        filename(str): name of the file
    '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
