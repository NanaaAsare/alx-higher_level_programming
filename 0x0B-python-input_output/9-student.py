#!/usr/bin/python3
'''9-student.py module'''


class Student:
    '''Defines a Student class'''

    def __init__(self, first_name, last_name, age):
        '''
        Initializes a Student class with first_name, last_name
        and age.

        Args:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
