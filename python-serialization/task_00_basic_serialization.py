#!/usr/bin/env python3
'''Basic Serialization'''
import json


def serialize_and_save_to_file(data, filename):
    '''Serialization function'''
    with open(filname, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    '''Deserialization function'''
    with open(filename, 'r') as file:
        return json.load(file)
