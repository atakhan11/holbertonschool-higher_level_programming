#!/usr/bin/python3
'''This Module about subclass Rectangle'''


class Rectangle(BaseGeometry):
    '''Class Rectangle'''
    def __init__(self, width, height):
        self.__width = width
        self.__height= height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
