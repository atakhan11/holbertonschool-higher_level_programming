#!/usr/bin/python3
'''This module writes string to a text file'''


def write_file(filename="", text=""):
    '''Write to file'''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
