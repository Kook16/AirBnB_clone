#!/usr/bin/python3
'''Tests for the base_mode module'''
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    '''Unit tests for the BaseModel class'''
    def setUp(self):
        self.model = BaseModel()
        self.model1 = BaseModel()

    def tearDown(self):
        # Remove the test file created during tests
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_id_is_string(self):
        self.assertTrue(isinstance(self.model.id, str))

    def test_id_len(self):
        self.assertEqual(len(self.model.id), 36)

    def test_id_equality_two_obj(self):
        self.assertNotEqual(self.model.id, self.model1.id)

    def test_created_at_is_datetime(self):
        self.assertTrue(isinstance(self.model.created_at, datetime))

    def test_updated_at_is_datetime(self):
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_to_dict_method(self):
        obj_dict = self.model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_str_method(self):
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_save_method_updates_updated_at(self):
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)

    def test_save_method_updates_file(self):
        self.model.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_save_method_updates_objects_dict(self):
        objects_dict = storage.all()
        self.model.save()
        new_objects_dict = storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
