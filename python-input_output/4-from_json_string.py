#!/usr/bin/python3
'''This module returns to object from JSON string'''
import json


def from_json_string(my_str):
    '''From JSON string to Object'''
    return json.loads(my_str)
