import unittest
from models.amenity import Amenity
import os
from models import storage, FileStorage


class Testamenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_amenity_instance(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_attributes(self):
        self.assertEqual(self.amenity.name, "")

    def test_amenity_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_str_method(self):
        expected = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected)

    def test_amenity_save_updates_file(self):
        self.amenity.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_amenity_save_updates_objects_dict(self):
        objects_dict = self.storage.all()
        self.amenity.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
