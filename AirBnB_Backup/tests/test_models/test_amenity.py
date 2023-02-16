import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    
    def setUp(self):
        """Set up test data for the Amenity class"""
        self.new_amenity = Amenity(name="Wifi")
        
    def test_instance(self):
        """Test the creation of a new Amenity instance"""
        self.assertIsInstance(self.new_amenity, Amenity)
        
    def test_name_attribute(self):
        """Test the name attribute of the Amenity class"""
        self.assertEqual(self.new_amenity.name, "Wifi")
        
    def test_save_method(self):
        """Test the save method of the Amenity class"""
        self.new_amenity.save()
        self.assertNotEqual(self.new_amenity.created_at, self.new_amenity.updated_at)
        
    def test_str_method(self):
        """Test the string representation of the Amenity class"""
        self.assertEqual(str(self.new_amenity), "[Amenity] ({}) {}".format(self.new_amenity.id, self.new_amenity.__dict__))

if __name__ == "__main__":
    unittest.main()

