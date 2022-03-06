#!/usr/bin/python3
"""Defines class named BaseModel"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base class from which other classes will derive from"""

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """print [<class name>] (<self.id>) <self.__dict__>"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """update instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dict containing values of self.__dict__"""
        self_attr = self.__dict__.copy()
        self_attr["__class__"] = self.__class__.__name__

        self_attr["created_at"] = self.created_at.isoformat("T", "auto")
        self_attr["updated_at"] = self.updated_at.isoformat("T", "auto")

        return self_attr
