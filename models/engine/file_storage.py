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

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                   "Place": Place, "Review": Review, "State": State,
                   "User": User}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                d_objects = json.load(f)
                for key, value in d_objects.items():
                    new_obj = classes[d_objects[key]["__class__"]](**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass
