#!/usr/bin/python3
'''This Module about subclass Square'''

BaseGeometry =__import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)
