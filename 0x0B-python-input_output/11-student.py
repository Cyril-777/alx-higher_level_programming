#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """student class class"""

    def __init__(self, first_name, last_name, age):
        """ Instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None and all(isinstance(a, str) for a in attrs):
            return {
                a: getattr(self, a) for a in attrs if hasattr(self, a)
            }
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
