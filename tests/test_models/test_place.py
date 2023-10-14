import unittest
from models.place import Place
import os
from models import FileStorage, storage


class TestState(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_review_instance(self):
        self.assertIsInstance(self.place, Place)
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_place_attributes(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_review_to_dict(self):
        state_dict = self.place.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'Place')

    def test_review_str_method(self):
        expected = f"{[Place]} ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected)

    def test_review_save_updates_file(self):
        self.place.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_review_save_updates_objects_dict(self):
        objects_dict = self.storage.all()
        self.place.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
