#!/usr/bin/python3
'''This module about is Pickling custom Classes'''
import pickle


class CustomObject:
    '''Class CustomObject'''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student


    def display(self):
        '''Display method for print object's attributes'''
        print({self.name})
        print({self.age})
        print({self.is_student})


    def serialize(self, filename):
        '''Serialize method'''
        with open(filename, 'w', encoding="utf-8") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        '''Deserialize method'''
        with open(filename, 'r', encoding="utf-8") as file:
            return pickle.load(cls, file)
