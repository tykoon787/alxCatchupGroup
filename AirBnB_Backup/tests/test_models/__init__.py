import unittest

class TestInitFile(unittest.TestCase):
    def test_import_models(self):
        try:
            import models
        except ImportError:
            self.fail("Failed to import models module")
    
    def test_import_engine(self):
        try:
            from models import engine
        except ImportError:
            self.fail("Failed to import engine module from models")

if __name__ == '__main__':
    unittest.main()

