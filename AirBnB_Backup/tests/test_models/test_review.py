import unittest
import models
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()
        
    def test_review_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_review_id(self):
        self.assertIsNotNone(self.review.id)

    def test_review_created_at(self):
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertEqual(self.review.created_at, self.review.updated_at)

    def test_review_updated_at(self):
        old_updated = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated, self.review.updated_at)

    def test_review_to_dict(self):
        self.assertIsInstance(self.review.to_dict(), dict)

if __name__ == "__main__":
    unittest.main()

