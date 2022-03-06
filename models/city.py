#!/usr/bin/python3
"""Defines a class named City"""

from models.base_model import BaseModel


class City(BaseModel):
    """child class of BaseModel"""
    state_id = ""
    name = ""
