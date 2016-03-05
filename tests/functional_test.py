import random
import unittest

from .. import analytics
from .. import io_geojson
from .. import utils
from .. import point


class TestFunctionalPointPattern(unittest.TestCase):

    def setUp(self):
        random.seed(12345)
        i = 0
        self.points = []
        marks = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        while i < 100:
            seed = (round(random.random(),2), round(random.random(),2))
            self.points.append(point.Point(
                seed[0],                        # Random x coordinate
                seed[1],                        # Random y coordinate
                color=random.choice(marks)))    # Random mark

            n_additional = random.randint(5,10)
            i += 1
            c = random.choice([0,1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt = (round(seed[0] + x_offset, 2), round(seed[1] + y_offset,2))
                    self.points.append(point.Point(pt[0], pt[1], color=random.choice(marks)))
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break

    def test_point_pattern(self):
        """
        This test checks that the code can compute an observed mean
         nearest neighbor distance and then use Monte Carlo simulation to
         generate some number of permutations.  A permutation is the mean
         nearest neighbor distance computed using a random realization of
         the point process.
        """
        random.seed()  # Reset the random number generator using system time

        observed_avg = analytics.average_nearest_neighbor_distance(self.points)

        self.assertAlmostEqual(0.033, observed_avg, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = utils.create_random(100)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = analytics.permutations(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = analytics.compute_critical(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

        # As above, update the module and function name.
        significant = utils.check_significant(lower, upper, observed_avg)
        self.assertTrue(significant)

    def test_marked_point_pattern(self):
        """
        Performs the same tests as test_point_pattern, but takes into consideration
        different marks.
        """
        marks = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

        random.seed()  # Reset the random number generator using system time

        expected_results = {
            'red': 0.116,
            'orange': 0.055,
            'yellow': 0.085,
            'green': 0.087,
            'blue': 0.126,
            'indigo': 0.179,
            'violet': 0.150
        };
        for mark in marks:
            observed_avg = analytics.average_nearest_neighbor_distance(self.points, mark)
            self.assertAlmostEqual(expected_results[mark], observed_avg, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = utils.create_random(100)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        for mark in marks:
            # As above, update the module and function name.
            permutations = analytics.permutations(99)
            self.assertEqual(len(permutations), 99)
            self.assertNotEqual(permutations[0], permutations[1])

            lower, upper = analytics.compute_critical(permutations)
            self.assertTrue(lower > 0.03)
            self.assertTrue(upper < 0.07)
            self.assertTrue(observed_avg < lower or observed_avg > upper)

            # As above, update the module and function name.
            significant = utils.check_significant(lower, upper, observed_avg)
            self.assertTrue(significant)