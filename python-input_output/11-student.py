#!/usr/bin/python3
class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of instance.

        If `attrs` is a list of strings, return only those attributes.
        Otherwise, return all public attributes.
        """
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the instance from a dictionary."""
        for key in json:
            setattr(self, key, json[key])

