#!/usr/bin/python3
'''This module is about reading file'''


def read_file(filename=""):
    '''Read file function'''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
