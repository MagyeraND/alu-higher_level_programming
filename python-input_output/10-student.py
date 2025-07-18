#!/usr/bin/python3
class Student:
    """Defines a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance
        
        If attrs is a list of strings, only returns keys matching those.
        Otherwise, returns the full __dict__.
        """
        if (type(attrs) == list and
            all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

