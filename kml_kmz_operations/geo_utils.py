import math

def dist(pt1, pt2):
    #haversine formula (https://en.wikipedia.org/wiki/Haversine_formula)
    R = 6378.1

    [phi1, lam1] = [math.radians(pt1[0]), math.radians(pt1[1])]
    [phi2, lam2] = [math.radians(pt2[0]), math.radians(pt2[1])]
    d = (2 * R *
         math.asin(math.sqrt(math.sin((phi2 - phi1) / 2)**2 +
                             math.cos(phi1) * math.cos(phi2) *
                             math.sin((lam2 - lam1) / 2)**2)))
    return d
