'''Tests for the city module'''
import unittest
from models.city import City
import os
from models import storage, FileStorage


class TestCity(unittest.TestCase):
    '''Unit tests for the City class'''
    def setUp(self):
        '''setup method'''
        self.city = City()
        self.storage = FileStorage()

    def tearDown(self):
        '''teardown method'''
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_city_instance(self):
        '''Test for instances'''
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_attributes(self):
        '''Tests for attributes'''
        self.assertEqual(self.city.name, "")

    def test_city_to_dict(self):
        '''Tests for to_dict method'''
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

    def test_city_str_method(self):
        '''Tests for str method'''
        expected = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected)

    def test_city_save_updates_file(self):
        '''tests for the save method'''
        self.city.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_city_save_updates_objects_dict(self):
        '''Tests for update method '''
        objects_dict = self.storage.all()
        self.city.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
