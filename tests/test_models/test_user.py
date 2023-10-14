#!/usr/bin/python3
'''Tests for the user module'''
import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    '''Unit tests for the Amenity class'''
    def setUp(self):
        self.user = User()
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_user_instance(self):
        '''Test for instances'''
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_attributes(self):
        '''Tests for attributes'''
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_to_dict(self):
        '''Tests for to_dict method'''
        user_dict = self.user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_user_str_method(self):
        '''Tests for str method'''
        expected = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected)

    def test_user_save_updates_file(self):
        '''tests for the save method'''
        self.user.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_user_save_updates_objects_dict(self):
        '''Tests for update method '''
        objects_dict = self.storage.all()
        self.user.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
