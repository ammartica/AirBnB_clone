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
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        with open(self.__file_path, 'r', encoding='utf-8') as f:
            json.load(f)
