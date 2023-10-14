#!/usr/bin/python3
'''Tests for the state module'''
import unittest
from models.state import State
import os
from models import storage, FileStorage


class TestState(unittest.TestCase):
    '''Unit tests for the State class'''
    def setUp(self):
        self.state = State()
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_state_instance(self):
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_attributes(self):
        self.assertEqual(self.state.name, "")

    def test_state_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_state_str_method(self):
        expected = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected)

    def test_state_save_updates_file(self):
        self.state.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_state_save_updates_objects_dict(self):
        objects_dict = self.storage.all()
        self.state.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
