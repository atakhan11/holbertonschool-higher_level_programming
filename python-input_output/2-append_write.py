#!/usr/bin/python3
'''This module appends a string at the end of file'''


def append_write(filename="", text=""):
    '''Append to a file'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
