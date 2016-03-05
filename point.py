from . import utils
import random


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
