import unittest
from main import pow2

class MyTest(unittest.TestCase):
    def test_pow2(self):
        
        x = 4
        y = 16

        n = pow2(x)

        self.assertEqual(n, y)