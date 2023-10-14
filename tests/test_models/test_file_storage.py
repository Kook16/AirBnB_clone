#!/usr/bin/python3
'''Tests for the Filestorage module'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''Unit tests for the TestFileStorage class'''
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.id = "test-id"

    def test_init(self):
        '''Tests for the value of name attr'''
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_new_method(self):
        self.storage.new(self.base_model)
        self.assertIn("BaseModel.test-id", self.storage._FileStorage__objects)

    def test_all_method(self):
        self.storage.new(self.base_model)
        all_objs = self.storage.all()
        self.assertEqual(all_objs["BaseModel.test-id"], self.base_model)

    def test_save_method(self):
        self.storage.new(self.base_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as file:
            data = file.read()
        self.assertIn("BaseModel.test-id", data)

    def test_reload_method(self):
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.test-id", all_objs)


if __name__ == '__main__':
    unittest.main()
