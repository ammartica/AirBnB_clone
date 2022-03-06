#!/usr/bin/python3
"""Defines a class named Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """child class of BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
