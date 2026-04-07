#!/usr/bin/python3
'''This Module containing integer validator'''


class BaseGeometry:
    '''BaseGeometry class'''

    def area(self):
        '''Raises Exception if area() is not implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates that value is an integer > 0 (but not bool)'''
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
