#!/usr/bin/python3
'''This module writes an OBject to a text file'''
import json


def save_to_json_file(my_obj, filename):
    '''Save Object to a file'''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
