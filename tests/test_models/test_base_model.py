#!/usr/bin/python3
""" base_model Test Suite """


import unittest
from models.base_model import BaseModel
import re
from datetime import datetime, timedelta


class Test_Base_Model(unittest.TestCase):
    """ Test Cases for Base_Model class"""

    regex_id = ""
    attr_dic = {"id": str, "created_at": datetime, "update_at": datetime}

    def setup(self):
        """ Sets up all tests """
        Test_Base_Model.regex_id = "BaseModel.[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-\
                                    [0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]\
                                    {12}"

    def test_default_values(self):
        """ uuid has correct format """
        my_model = BaseModel()
        is_match = bool(re.match(Test_Base_Model.regex_id, my_model.id))
        self.assertTrue(is_match, "id is in wrong format")

    def test_attributes_set(self):
        """ Setting attributes assigns values given """
        my_model1 = BaseModel()
        my_model1.name = "My First Model"
        my_model1.my_number = 89
        self.assertEqual(my_model1.name, "My First Model")
        self.assertEqual(my_model1.my_number, 89)

    def test_passing_dict(self):
        """ Passing a dictionary of values sets propper attributes """
        todaydt = datetime.today()
        yesterdaydt = todaydt - timedelta(days=1)

        # turn values into

        today = todaydt.isoformat("T", "auto")
        yesterday = yesterdaydt.isoformat("T", "auto")

        values = {"id": "THIS IS AN ID", "created_at": yesterday,
                  "updated_at": today}
        my_model = BaseModel(**values)

        values["updated_at"] = todaydt
        values["created_at"] = yesterdaydt

        self.assertEqual(values["id"], my_model.id)
        self.assertEqual(values["created_at"], my_model.created_at)
        self.assertEqual(values["updated_at"], my_model.updated_at)


if __name__ == '__main__':
    unittest.main()
