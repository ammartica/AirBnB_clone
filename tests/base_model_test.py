#!/usr/bin/python3
""" base_model Test Suite """


import unittest
from models.base_model import BaseModel

class Test_Base_Model(unittest.TestCase):
    """ Test Cases for Base_Model class"""

    def setup(self):
        self.my_model = BaseModel()

    def test_attributes_set(self):
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)

if __name__ == '__main__':
    unittest.main()
