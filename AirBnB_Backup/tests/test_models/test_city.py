import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test for the City class"""

    def setUp(self):
        """Sets up an instance of the City class before each test"""
        self.city = City()

    def tearDown(self):
        """Deletes the instance of the City class after each test"""
        del self.city

    def test_city_instance(self):
        """Tests if the City class creates a new instance of the City class"""
        self.assertIsInstance(self.city, City)

    def test_city_attributes(self):
        """Tests if the City class has the correct class attributes"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_city_str(self):
        """Tests the string representation of the City class"""
        self.assertEqual(str(self.city), "[City] ({}) {}".format(self.city.id, self.city.__dict__))

