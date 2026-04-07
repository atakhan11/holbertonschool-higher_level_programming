#!/usr/bin/python3
'''This Module containing inherited from'''


def inherits_from(obj, a_class):
    '''Function to check only sub class'''
    return isinstance(obj, a_class) and type(obj) is not a_class
