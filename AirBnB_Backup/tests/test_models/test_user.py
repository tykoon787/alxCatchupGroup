import unittest
import models
from models.user import User

class TestUser(unittest.TestCase):
    """Test for the User class"""

    def setUp(self):
        """Sets up a user instance for the tests"""
        self.user = User()
    
    def test_attributes(self):
        """Tests for the existence of expected attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_init(self):
        """Tests that the user instance is correctly initialised"""
        self.assertTrue(isinstance(self.user, User))

    def test_str(self):
        """Tests the output of str method"""
        self.assertEqual(str(self.user),
                         "[User] ({}) {}".format(self.user.id, self.user.__dict__))

    def test_to_dict(self):
        """Tests the output of the to_dict method"""
        expected_dict = {"id": self.user.id,
                         "email": self.user.email,
                         "password": self.user.password,
                         "first_name": self.user.first_name,
                         "last_name": self.user.last_name,
                         "created_at": self.user.created_at.isoformat(),
                         "updated_at": self.user.updated_at.isoformat(),
                         "__class__": "User"}
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_save(self):
        """Tests the output of the save method"""
        self.user.save()
        self.assertNotEqual(self.user.updated_at, self.user.created_at)

if __name__ == "__main__":
    unittest.main()

