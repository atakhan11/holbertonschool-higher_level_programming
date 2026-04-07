#!/usr/bin/python3
'''This Module print sorted list'''


class MyList(list):
    '''Class inherited from list class'''
    def print_sorted(self):
        print(sorted(self))
