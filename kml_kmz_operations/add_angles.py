#!/bin/python3

from pprint import pprint
import argparse
import zipfile
import math
import os
import re


def get_file_contents(file_path):

    if file_path.endswith('.kml'):

        with open(file_path, 'r') as fp:
            return fp.read()

    elif file_path.endswith('.kmz'):

        with zipfile.ZipFile(file_path, 'r') as zip:

            return zip.read('doc.kml').decode()


def save_to_kmz(file_path, text):

    with zipfile.ZipFile(file_path, 'w') as zip:

        zip.write('doc.kml', text)


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


def extract_polygons(kml_str):
    poly_list = []
    for poly in re.findall(r'<Polygon>.*</Polygon>', kml_str, re.DOTALL):
        poly_list.append(poly)
    return poly_list


def extract_coordinates(poly_str):

    coordinates = []

    for coor_str in re.findall(r'[\-0-9\.]+,[\-0-9.]+,[\-0-9.]+', poly_str):

        lon, lat, alt = coor_str.split(',')
        lat, lon = float(lat), float(lon)
        if (lat, lon) not in coordinates:
            coordinates.append((lat, lon))
    return coordinates


def getDifference(b1, b2):
    r = (b2 - b1) % 360.0
    # Python modulus has same sign as divisor, which is positive here,
    # so no need to consider negative case
    if r >= 180.0:
        r -= 360.0
    return r


def make_placemark(latlon, name):

    point = """
    <Placemark>
    <name>{name}</name>
    <Point>
        <coordinates>{lon},{lat},0</coordinates>
    </Point>
    </Placemark>
    """.format(lat=latlon[0], lon=latlon[1], name=name)
    return point


def get_angles(coordinates, debug_mode=False):
    placemarks = []
    num_coor = len(coordinates)
    angles = []
    for cur_index in range(len(coordinates)):
        prev_i = (cur_index - 1) % num_coor
        nex_i = (cur_index + 1) % num_coor
        prev = coordinates[prev_i]
        cur = coordinates[cur_index]
        nex = coordinates[nex_i]

        brng_1 = get_bearing(cur, prev)

        brng_2 = get_bearing(cur, nex)

        angle = getDifference(brng_1, brng_2)

        angles.append(angle)

        if debug_mode:
            p_c = ((cur[0] + prev[0])/2, (cur[1] + prev[1])/2)
            placemarks.append(make_placemark(
                p_c,
                '({}->{}){}'.format(cur_index, prev_i, brng_1)))
            c_n = ((cur[0] + nex[0])/2, (cur[1] + nex[1])/2)
            placemarks.append(make_placemark(
                c_n,
                '({}->{}){}'.format(cur_index, nex_i, brng_2)))

            placemarks.append(make_placemark(cur, '({})'.format(cur_index)))
        placemarks.append(make_placemark(cur, '{0:0.3f}'.format(angle)))
    # the theoritical sum of the interior angles of a polygon is
    expected_sum = 180 * (num_coor - 2)
    if sum(angles) - expected_sum > 0.01:
        print('Unexpected!')
    return placemarks


def run():

    parser = argparse.ArgumentParser('parser for adding angles to kml and kmz')
    parser.add_argument(
        'fp', type=str, nargs='?',
        help='Please provide the path to the kml/kmz file to add angles to')
    parser.add_argument(
        '-debug', action='store_true', default=False, help='Run in debug mode')

    args = parser.parse_args()

    file_path = args.fp

    kml_str = get_file_contents(file_path)
    poly_list = extract_polygons(kml_str)

    pins = []
    for p in poly_list:
        coordinates = extract_coordinates(p)
        pins.extend(get_angles(coordinates, args.debug))

    kml_prefix, kml_postfix = kml_str.split('</Document>')

    final_kml = kml_prefix + ''.join(pins) + '</Document>' + kml_postfix

    folder = os.path.dirname(file_path)
    fname = os.path.basename(file_path)
    output_name = '{}_angles.kml'.format(fname.split('.')[0])

    with open(os.path.join(folder, output_name), 'w') as kmlfile:
        kmlfile.write(final_kml)


if __name__ == "__main__":
    run()
