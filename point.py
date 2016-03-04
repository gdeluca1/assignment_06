from . import utils
import random


def create_random_marked_points(n, marks=[]):
    random.seed(12345)
    points = []
    i = 0
    while i < n:
        seed = (round(random.random(),2), round(random.random(),2))
        points.append(Point(
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
                points.append(Point(pt[0], pt[1], color=random.choice(marks)))
                i += 1
                if i == n:
                    break
        if i == n:
            break
    return points


class Point(object):
    def __init__(self, x, y, **mark):
        self.x = x
        self.y = y
        self.mark = mark

    def is_coincident(self, other_point):
        return utils.check_coincident((self.x, self.y), (other_point.x, other_point.y))

    def shift_point(self, delta_x, delta_y):
        result = utils.shift_point((self.x, self.y), delta_x, delta_y)
        self.x = utils.getx(result)
        self.y = utils.gety(result)
