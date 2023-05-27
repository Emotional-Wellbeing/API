import unittest

from src.utils import data_not_empty


class TestUtils(unittest.TestCase):
    def testDataNotEmptyEmptyData(self):
        data = {"1": [], "2": [], "3": [], "4": []}
        self.assertFalse(data_not_empty(data), "This dict doesn't contain data")

    def testDataNotEmptyNotEmptyData(self):
        data = {"1": [], "2": [], "3": [], "4": [""]}
        self.assertTrue(data_not_empty(data), "This dict contain data")
