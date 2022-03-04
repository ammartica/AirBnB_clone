#!/usr/bin/python3
"""Defines class named FileStorage"""

import json

class FileStorage:
    """Class serializes/deserializes instances to JSON file and back"""
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
        for item in self.__objects:
            nested_objs[item] = {}
            for key, value in self.__objects[item].to_dict().items():
                nested_objs[item][key] = value
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(nested_objs, f)

#this function is likely wrong because I am very confused
#about deserializing a nested dict into a regular dict
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                d_objects = json.load(f)
                for key in d_objects:
                    class_name = getattr(models, d_objects[key]['__class__'])
                    new_obj = class_name(d_objects)
                    self.new(new_obj)
        except FileNotFoundError:
            pass
