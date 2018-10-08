#!/bin/python3
from typing import List, Tuple
import argparse
import re

import zipfile

import os

import simplekml
import math
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_bearing(l1, l2):

    # convert decimal degrees to radians
    [phi1, lam1] = [math.radians(l1[0]), math.radians(l1[1])]
    [phi2, lam2] = [math.radians(l2[0]), math.radians(l2[1])]
    y = math.sin(lam2 - lam1) * math.cos(phi2)
    x = (math.cos(phi1) * math.sin(phi2) -
         math.sin(phi1) * math.cos(phi2) * math.cos(lam2 - lam1))

    bearing = math.degrees(math.atan2(y, x))
    if bearing > 180:
        bearing -= 360
    return bearing


def extract_coordinates(poly_str):

    coordinates = []

    for coor_str in re.findall(r'[\-0-9\.]+,[\-0-9.]+,[\-0-9.]+', poly_str):

        lon, lat, alt = coor_str.split(',')
        lat, lon = float(lat), float(lon)
        if (lat, lon) not in coordinates:
            coordinates.append((lat, lon))
    return coordinates


def get_file_contents(file_path):

    if file_path.endswith('.kml'):

        with open(file_path, 'r') as fp:
            return fp.read()

    elif file_path.endswith('.kmz'):

        with zipfile.ZipFile(file_path, 'r') as zip:

            return zip.read('doc.kml').decode()


def extract_polygons(kml_str):
    poly_list = []
    for poly in re.findall(r'<Polygon>.*</Polygon>', kml_str, re.DOTALL):
        poly_list.append(poly)
    return poly_list


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


def get_destination(origin, brng, d):
    """Given an origin, bearing and distance, return destination.

    Args:
        origin : (lat, lon)
        brng : bearing, in degrees
        d : distance, in kms
    """
    R = 6378.1
    brng_r = math.radians(brng)
    [phi1, lam1] = [math.radians(origin[0]), math.radians(origin[1])]
    phi2 = math.asin(math.sin(phi1) * math.cos(d / R) +
                     math.cos(phi1) * math.sin(d / R) * math.cos(brng_r))
    lam2 = lam1 + math.atan2(math.sin(brng_r) * math.sin(d / R) *
                             math.cos(phi1), math.cos(d / R) -
                             (math.sin(phi1) * math.sin(phi2)))
    return (math.degrees(phi2), math.degrees(lam2))


def get_coordinates(file_path: str) -> List[Tuple[float, float]]:

    kml_str = get_file_contents(file_path)
    polygon = extract_polygons(kml_str)[0]

    coordinates = extract_coordinates(polygon)
    return coordinates


def get_bbox(coordinates):
    lats, lons = [], []
    for co in coordinates:
        lats.append(co[0])
        lons.append(co[1])
    lats = [co[0] for co in coordinates]
    lons = [co[0] for co in coordinates]
    min_lat = min(lats)
    max_lat = max(lats)
    min_lon = min(lons)
    max_lon = max(lons)
    return min_lat, max_lat, min_lon, max_lon


def pick_vertex(coordinates, origin_i):

    origin = coordinates[origin_i]
    prev = coordinates[origin_i - 1]
    next = coordinates[(origin_i + 1) % len(coordinates)]

    bearing1 = get_bearing(origin, prev)
    bearing2 = get_bearing(origin, next)

    return origin, (prev, bearing1), (next, bearing2)


class make_opposite_boundry:

    def __init__(self, pt1, pt2):
        if pt1[1] > pt2[1]:
            print('flipping')
            pt1, pt2 = pt2, pt1

        self.lat1 = pt1[0]
        self.lon1 = pt1[1]
        self.lat2 = pt2[0]
        self.lon2 = pt2[1]

        self.m = (self.lat2 - self.lat1) / (self.lon2 - self.lon1)
        self.b = self.lat1

    def cal_lat(self, lon):

        adjusted_lon = lon - self.lon1
        return (adjusted_lon * self.m) + self.b

    def intersection(self, line2):

        lon = (self.b - line2.b) / (line2.m - self.m)
        lon_intersect = lon + self.lon1
        return lon_intersect


def geo_to_Point(pt):

    newx = int(pt[0] * 1000)
    newy = int(pt[1] * 1000)
    return Point(newx, newy)


class Polygon_hitbox:

    def __init__(self, coordinates):
        self.coordinates = [geo_to_Point(pt) for pt in coordinates]

        self.num_verticies = len(coordinates)
        min_lat, max_lat, min_lon, max_lon = get_bbox(coordinates)

        self.outside_pt = geo_to_Point((min_lat, min_lon))

    def is_inside(self, geo_pt: Tuple[float, float]) -> bool:

        pt = geo_to_Point(geo_pt)

        # count the number of intersections
        count = 0

        for i in range(self.num_verticies):

            next = (i + 1) % self.num_verticies

            segment_a = self.coordinates[i]
            segment_b = self.coordinates[next]

            if doIntersect(self.outside_pt, pt, segment_a, segment_b):
                count += 1

        return count % 2 == 1


def cli():
    parser = argparse.ArgumentParser('get evenly distributed points for a '
                                     'arbitrary polygon radiating from the '
                                     'specified vertex')
    parser.add_argument('file_path', type=str,
                        help='Please provide the path to the kml/kmz file with'
                        ' the kml/kmz defining the polygon')
    parser.add_argument('vertex', type=int,
                        help='Index of the coordinate you want to use as the '
                        ' origin')

    parser.add_argument('-degree', nargs='?', default=0.5, type=float,
                        help="optional size angle between successive lines")
    parser.add_argument('-spacing', nargs='?', default=1, type=float,
                        help="optional value for the distance between points")
    args = parser.parse_args()
    return args


def run(args):

    kml_root = simplekml.Kml()

    fp = args.file_path
    angle_interval = args.degree
    vert_i = args.vertex
    spacing = args.spacing
    initial_gap = 1
    logger.info(f'loading polygon from {fp}')

    coordinates = get_coordinates(fp)

    intersect_test = Polygon_hitbox(coordinates)
    logger.debug(f'origin vertex index is {vert_i}')
    origin, bound1, bound2 = pick_vertex(coordinates, vert_i)

    pt1, current_bearing = bound1
    pt2, final_bearing = bound2
    bline = make_opposite_boundry(pt1, pt2)

    lon_var = (pt2[1] - pt1[1]) / 10.0
    boundry_folder = kml_root.newfolder(name="opposite side")

    boundry_lon = pt1[1]
    while boundry_lon < pt2[1]:

        bpt = [bline.cal_lat(boundry_lon), boundry_lon]
        boundry_lon += lon_var
        boundry_folder.newpoint(coords=[bpt[::-1]])

    if final_bearing < current_bearing:
        final_bearing += 360
        logger.debug('bearing swap!')
    line_number = 0

    while current_bearing < final_bearing:
        logger.debug(current_bearing)
        line_folder = kml_root.newfolder(name=f'line{line_number}')
        line_number += 1
        distance = initial_gap

        next_coordinate = get_destination(origin, current_bearing, distance)

        while intersect_test.is_inside(next_coordinate):

            line_folder.newpoint(
                coords=[[next_coordinate[1], next_coordinate[0]]],
            )

            distance += spacing
            next_coordinate = get_destination(origin, current_bearing,
                                              distance)
        current_bearing += angle_interval

    output_file = f'output{args.vertex}.kml'
    logger.info('saving ' + output_file)
    kml_root.save(output_file)

args = cli()

fp = args.file_path
angle_interval = args.degree
vert_i = args.vertex
spacing = args.spacing

run(args)
