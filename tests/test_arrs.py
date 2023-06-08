import unittest
from utils import arrs
from utils.arrs import get, my_slice


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(get([1, 2, 3, 4, 5], 3, "test"), 4)
        self.assertEqual(get([1, 2, 3, 4, 5], 4, "test"), 5)
        self.assertEqual(get([], -1, "test"), "test")





        #self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 3)
        #self.assertEqual(arrs.get([], 0, "test"), "test")


    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([], 0), [])
        self.assertEqual(my_slice([2], 0), [2])
        self.assertEqual(my_slice([1, 2, 3], -2), [2, 3])
        self.assertEqual(my_slice([1], -2), [1])


