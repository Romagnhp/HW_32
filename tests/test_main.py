import unittest
from main import mySum, myAveage, myMaxElement, myMinElement

class MyTest(unittest.TestCase):
    def test_mySum(self):
        self.assertEqual(mySum(5,5), 10)

    def test_myAverage(self):
        self.assertEqual(myAveage(5,1,3), 3)

    def test_myMaxElement(self):
        self.assertEqual(myMaxElement(5,8,0,1), 8)

    def test_myMinElement(self):
        self.assertEqual(myMinElement(5,8,-1,1), -1)