import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics


class TestAnalytics(unittest.TestCase):

    def setUp(self):
        pass

    def test_permutations(self):
        self.assertEqual(len(analytics.permutations(300)), 300)

    def test_critical(self):
        criticals = analytics.compute_critical([0.5, 1.0, 0.99, 3.14, 0.987, 0.102])
        self.assertTrue(criticals[0] == 0.102 and criticals[1] == 3.14)