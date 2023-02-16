import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class"""

    def setUp(self):
        """Sets up test cases"""
        self.test_base_model = BaseModel()

    def test_to_dict(self):
        """Tests the to_dict method of BaseModel"""
        test_dict = self.test_base_model.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)

    def test_id(self):
        """Tests the id attribute of BaseModel"""
        self.assertEqual(str, type(self.test_base_model.id))

    def test_created_at(self):
        """Tests the created_at attribute of BaseModel"""
        self.assertEqual(datetime, type(self.test_base_model.created_at))

    def test_updated_at(self):
        """Tests the updated_at attribute of BaseModel"""
        self.assertEqual(datetime, type(self.test_base_model.updated_at))

    def test_save(self):
        """Tests the save method of BaseModel"""
        before = self.test_base_model.updated_at
        self.test_base_model.save()
        after = self.test_base_model.updated_at
        self.assertNotEqual(before, after)

if __name__ == '__main__':
    unittest.main()

