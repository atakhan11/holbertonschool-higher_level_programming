#!/usr/bin/python3
'''This module creating class'''


class Square:
    '''Creating private attribute'''
    def __init(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
