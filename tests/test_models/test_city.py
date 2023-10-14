import unittest
from models.city import City
import os
from models import storage, FileStorage


class Testcity(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_city_instance(self):
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_attributes(self):
        self.assertEqual(self.city.name, "")

    def test_city_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

    def test_city_str_method(self):
        expected = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected)

    def test_city_save_updates_file(self):
        self.city.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_city_save_updates_objects_dict(self):
        objects_dict = self.storage.all()
        self.city.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
