#!/bin/python3

from typing import List, Tuple

class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def onSegment(p: Point, q: Point, r: Point) -> bool:
    """
    Given three colinear points p, q, r, the function checks if
    point q lies on line segment 'pr'
    """

    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
            q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    return False


def orientation(p: Point, q: Point, r: Point) -> int:
    """
    To find orientation of ordered triplet (p, q, r).
    Returns:
        0 --> p, q and r are colinear
        1 --> Clockwise
        2 --> Counterclockwise
    See https://www.geeksforgeeks.org/orientation-3-ordered-points/
    for details of below formula.
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val == 0:
        # colinear
        return 0

    if val > 0:
        # Clockwise
        return 1
    # Counterclockwise
    return 2


def doIntersect(p1: Point, q1: Point, p2: Point, q2: Point) -> bool:

    """
    The main function that returns true if line segment 'p1q1' and 'p2q2'
    intersect.
    """

    print(p1, q1, p2, q2)

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2) and (o3 != o4):
        return True

    # Special Cases

    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and onSegment(p1, p2, q1)):
        return True
    # p1, q1 and q2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and onSegment(p1, q2, q1)):
        return True
    # p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0 and onSegment(p2, p1, q2)):
        return True

    # p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0 and onSegment(p2, q1, q2)):
        return True
    return False


def test():
    p1 = Point(1, 1)
    q1 = Point(10, 1)

    p2 = Point(1, 2)
    q2 = Point(10, 2)

    assert not doIntersect(p1, q1, p2, q2)

    p1 = Point(10, 0)
    q1 = Point(0, 10)

    p2 = Point(0, 0)
    q2 = Point(10, 10)
    assert doIntersect(p1, q1, p2, q2)

    p1 = Point(-5, -5)
    q1 = Point(0, 0)

    p2 = Point(1, 1)
    q2 = Point(10, 10)
    assert not doIntersect(p1, q1, p2, q2)


if __name__ == "__main__":
    test()
