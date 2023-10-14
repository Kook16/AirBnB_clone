#!/user/bin/python3
'''Tests for the amenity module'''
import unittest
from models.amenity import Amenity
import os
from models import storage, FileStorage


class Testamenity(unittest.TestCase):
    '''Unit tests for the Amenity class'''
    def setUp(self):
        '''setup method'''
        self.amenity = Amenity()
        self.storage = FileStorage()

    def tearDown(self):
        '''teardown method'''
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_amenity_instance(self):
        '''Test for instances'''
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_attributes(self):
        '''Tests for to_dict method'''
        self.assertEqual(self.amenity.name, "")

    def test_amenity_to_dict(self):
        '''Tests for str method'''
        amenity_dict = self.amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_str_method(self):
        '''tests for the save method'''
        expected = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected)

    def test_amenity_save_updates_file(self):
        '''tests for the save method'''
        self.amenity.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_amenity_save_updates_objects_dict(self):
        '''Tests for update method '''
        objects_dict = self.storage.all()
        self.amenity.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
