#!/usr/bin/python3
'''3-to_json_string.py module'''


import json


def to_json_string(my_obj):
    '''
    A function that returns the JSON representation
    of a python object.

    Args:
        my_obj(object): object to serialize to json

    Return:
        json string
    '''

    return json.dumps(my_obj)
