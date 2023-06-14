#!/usr/bin/python3
'''4-from_json_string.py module'''


import json


def from_json_string(my_str):
    '''
    A function that returns python object from a json string

    Args:
        my_str(str): json string to convert to python object

    Return:
        python object
    '''
    return json.loads(my_str)
