#!/usr/bin/python3
""" base_model Test Suite """


import unittest
from models.base_model import BaseModel
import re

class Test_Base_Model(unittest.TestCase):
    """ Test Cases for Base_Model class"""

    regex_id = ""

    def setup(self):
        Test_Base_Model.my_model1 = BaseModel()
        Test_Base_Model.regex_id = r"BaseModel.[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"

    def test_default_values(self):
        my_model = BaseModel()
        is_match = bool(re.match(Test_Base_Model.regex_id, my_model.id))
        self.assertTrue(is_match, "id is in wrong format")

    def test_attributes_set(self):
        my_model1 = BaseModel()
        my_model1.name = "My First Model"
        my_model1.my_number = 89
        self.assertEqual(my_model1.name, "My First Model")
        self.assertEqual(my_model1.my_number, 89)

if __name__ == '__main__':
    unittest.main()
