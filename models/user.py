#!/usr/bin/python3
"""Defines class named User"""

from models.base_model import BaseModel


class User(BaseModel):
    """class that defines a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes a user"""
        super().__init__(*args, **kwargs)
