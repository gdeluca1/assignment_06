from .utils import *


def find_largest_city(gj):
    """
    Iterate through a geojson feature collection and
    find the largest city.  Assume that the key
    to access the maximum population is 'pop_max'.

    Parameters
    ----------
    gj : dict
         A GeoJSON file read in as a Python dictionary

    Returns
    -------
    city : str
           The largest city

    population : int
                 The population of the largest city
    """
    city = None
    max_population = 0
    for item in gj["features"]:
        props = item["properties"]
        if props["pop_max"] > max_population:
            max_population = props["pop_max"]
            city = props["adm1name"]

    return city, max_population


def average_nearest_neighbor_distance(points):
    """
    Given a set of points, compute the average nearest neighbor.

    Parameters
    ----------
    points : list
             A list of points in the form (x,y)

    Returns
    -------
    mean_d : float
             Average nearest neighbor distance

    References
    ----------
    Clark and Evan (1954 Distance to Nearest Neighbor as a
     Measure of Spatial Relationships in Populations. Ecology. 35(4)
     p. 445-453.
    """
    mean_d = 0
    temp_nearest_neighbor = None
    # Average the nearest neighbor distance of all points.
    for point in points:
        # Find the nearest neighbor to this point.
        for otherPoint in points:
            # You are not your own neighbor.
            if check_coincident(point, otherPoint):
                continue
            # To avoid multiple calculations, we'll cache the result.
            current_distance = euclidean_distance(point, otherPoint)
            # nearest neighbor will be None if this is the first neighbor we have iterated over.
            if temp_nearest_neighbor is None:
                temp_nearest_neighbor = current_distance
            elif temp_nearest_neighbor > current_distance:
                temp_nearest_neighbor = current_distance
        # At this point, we've found point's nearest neighbor distance.
        # Add in that distance.
        mean_d += temp_nearest_neighbor
        temp_nearest_neighbor = None

    # Divide by number of points.
    mean_d /= len(points)

    return mean_d


def permutations(p = 99):
    n = 100
    to_return = []
    for i in range(p):
        to_return.append(
            average_nearest_neighbor_distance(
                create_random(n)
            )
        )
    return to_return


def compute_critical(p):
    """
    Calculates the critical points (lowest distance and greatest distance) in a set of
    randomly generated permutations (created using permutations(p)).
    """
    return min(p), max(p)