import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test Place class"""

    def setUp(self):
        """Create instance of Place class before each test"""
        self.place = Place()

    def test_Place_is_instance(self):
        """Test if self.place is instance of Place"""
        self.assertIsInstance(self.place, Place)

    def test_Place_has_attribute_city_id(self):
        """Test if self.place has attribute city_id"""
        self.assertTrue(hasattr(self.place, "city_id"))

    def test_Place_has_attribute_user_id(self):
        """Test if self.place has attribute user_id"""
        self.assertTrue(hasattr(self.place, "user_id"))

    def test_Place_has_attribute_name(self):
        """Test if self.place has attribute name"""
        self.assertTrue(hasattr(self.place, "name"))

    def test_Place_has_attribute_description(self):
        """Test if self.place has attribute description"""
        self.assertTrue(hasattr(self.place, "description"))

    def test_Place_has_attribute_number_rooms(self):
        """Test if self.place has attribute number_rooms"""
        self.assertTrue(hasattr(self.place, "number_rooms"))

    def test_Place_has_attribute_number_bathrooms(self):
        """Test if self.place has attribute number_bathrooms"""
        self.assertTrue(hasattr(self.place, "number_bathrooms"))

    def test_Place_has_attribute_max_guest(self):
        """Test if self.place has attribute max_guest"""
        self.assertTrue(hasattr(self.place, "max_guest"))

    def test_Place_has_attribute_price_by_night(self):
        """Test if self.place has attribute price_by_night"""
        self.assertTrue(hasattr(self.place, "price_by_night"))

    def test_Place_has_attribute_latitude(self):
        """Test if self.place has attribute latitude"""
        self.assertTrue(hasattr(self.place, "latitude"))

    def test_Place_has_attribute_longitude(self):
        """Test if self.place has attribute longitude"""
        self.assertTrue(hasattr(self.place, "longitude"))

    def test_Place_has_attribute_amenity_ids(self):
        """Test if self.place has attribute amenity_ids"""
        self.assertTrue(hasattr(self.place, "amenity_ids"))

if __name__ == '__main__':
    unittest.main()

