#!/usr/bin/python3
"""Defines class named FileStorage"""

import json


class FileStorage:
    """Class serializes/deserializes instances to JSON file and back"""

    def __init__(self):
        """Initializes FileStorage with private instances"""
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file in a nested dict"""
        nested_objs = {}
        for key, value in self.__objects.items():
            nested_objs[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(nested_objs, f)

#this function is likely wrong because I am very confused
#about deserializing a nested dictionary into a regular dict
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                d_objects = json.load(f)
            for key, value in d_objects.items():
                self.__objects[key] = value
        except:
            pass