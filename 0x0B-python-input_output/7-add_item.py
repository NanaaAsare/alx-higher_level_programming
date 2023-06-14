#!/usr/bin/python3
'''7-add_item.py module'''


import sys
import json


if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

    all_arguments = sys.argv[1:]
    all_arguments_json = json.dumps(all_arguments)

    save_to_json_file(all_arguments, 'add_item.json')
