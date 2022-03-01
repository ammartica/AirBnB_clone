#!/usr/bin/python3
"""Defines class named BaseModel"""

from uuid import uuid4()
from datetime import datetime

class BaseModel:
    """Base class from which other classes will derive from"""

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
       # self.updated_at = #assign with the current datetime when an instance is created and it will be updated every time you change your object

    def __str__(self):
        """print [<class name>] (<self.id>) <self.__dict__>"""
        return "[{:s}] ({:s}] {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        self_attr = self.__dict__.copy()
        self_attr["__class__"] = self.__class__.__name__

        iso_created_at = self.created_at.datetime.isoformat("T", "auto")
        iso_updated_at = self.updated_at.datetime.isoformat("T", "auto")

        self_attr["created_at"] = iso_created_at
        self_attr["updated_at"] = iso_updated_at
