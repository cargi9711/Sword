import unittest
from sword import Sword

class TestSword(unittest.TestCase):
    def test_swing(self):
        s = Sword("Test", 50, 2)
        self.assertIn("damage", s.swing())

if __name__ == "__main__":
    unittest.main()
