import os
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up method for testing the class"""
        self.file_storage = FileStorage()

    def test_file_path(self):
        """Test the file path"""
        self.assertEqual(self.file_storage._FileStorage__file_path,
                         "file.json")

    def test_objects(self):
        """Test the objects attribute"""
        self.assertEqual(self.file_storage._FileStorage__objects, {})

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.assertIn(obj, self.file_storage.all().values())

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        self.file_storage.__objects = {}
        self.file_storage.reload()
        self.assertIn(obj, self.file_storage.all().values())

if __name__ == "__main__":
    unittest.main()

