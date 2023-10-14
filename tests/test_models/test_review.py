import unittest
from models.review import Review
from models import FileStorage, storage
import os


class TestState(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up any created files or objects
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_review_instance(self):
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_attributes(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_to_dict(self):
        state_dict = self.review.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'Review')

    def test_review_str_method(self):
        expected = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected)

    def test_review_save_updates_file(self):
        self.review.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_review_save_updates_objects_dict(self):
        objects_dict = self.storage.all()
        self.review.save()
        new_objects_dict = self.storage.all()
        self.assertEqual(objects_dict, new_objects_dict)


if __name__ == '__main__':
    unittest.main()
