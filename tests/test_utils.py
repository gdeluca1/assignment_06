import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_random(self):
        self.assertEqual(len(utils.create_random(1000)), 1000)

    def test_check_significant(self):
        self.assertTrue(utils.check_significant(10, 30, 9.9))
        self.assertFalse(utils.check_significant(9.9, 30, 10))