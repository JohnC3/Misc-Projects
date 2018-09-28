import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def rgb_to_kml(R, G, B):
    """
    Convert the R, G, B colors to a kml color string, In kml RGB colors are stored
    in reverse order as hex values: IE TTBBGGRR (transparency blue green red)
    the reverse of the normal format.
    """
    R, G, B = int(R), int(G), int(B)
    kml_color_str = 'FF'  # TODO: Add support for transparency
    for v in [B, G, R]:
        hex_str = hex(v)

        hex_str = hex_str.replace('0x', '')
        pad = 2 - len(hex_str)
        kml_color_str += '0' * pad + hex_str

    return kml_color_str.upper()


def rgb_to_hsv(R, G, B):
    """
    Math comes from wikipedia Aug 9 2018
    https://en.wikipedia.org/wiki/HSL_and_HSV
    Takes the usual 0 - 255 rgb values we have come to begrudgingly accept
    And turn them to hsv values for better color gradients

    Args:
        rgb: A tuple containing the (R, G, B) values as numbers from 0 to 255
    Returns:
        H, S, V: The hue saturation value color
    """
    assert 0 <= R <= 255, f'Unexpected R {R}'
    assert 0 <= G <= 255, f'Unexpected G {G}'
    assert 0 <= B <= 255, f'Unexpected B {B}'

    R, G, B = R / 255.0, G / 255.0, B / 255.0

    M = max([R, G, B])
    m = min([R, G, B])
    C = M - m  # Chroma value
    if C == 0:
        # Should be undefined return R instead
        Hp = 0
    elif M == R:
        Hp = ((G - B) / C) % 6
    elif M == G:
        Hp = ((B - R) / C) + 2
    elif M == B:
        Hp = ((R - G) / C) + 4

    H = 60.0 * Hp
    V = M  # For HSV specifically

    if V == 0:
        S = 0
    else:
        S = C / V
    return H, S, V


def hsv_to_rgb(H, S, V):
    """
    Math comes from wikipedia Aug 9 2018
    https://en.wikipedia.org/wiki/HSL_and_HSV

    Convert hsv values back to the usual R, G, B values
    """
    if H < 0:
        H = 360 + H
    Hp = H / 60.0
    C = V * S

    X = C * (1 - abs((Hp % 2) - 1))

    if 0 <= Hp <= 1:
        Rp, Gp, Bp = (C, X, 0)
    elif 1 < Hp <= 2:
        Rp, Gp, Bp = (X, C, 0)
    elif 2 < Hp <= 3:
        Rp, Gp, Bp = (0, C, X)
    elif 3 < Hp <= 4:
        Rp, Gp, Bp = (0, X, C)
    elif 4 < Hp <= 5:
        Rp, Gp, Bp = (X, 0, C)
    elif 5 < Hp <= 6:
        Rp, Gp, Bp = (C, 0, X)
    else:
        raise ValueError("Invalid Hp value {}".format(Hp))
    m = V - C
    R = Rp + m
    G = Gp + m
    B = Bp + m

    R, G, B = round(R * 255), round(G * 255), round(B * 255)
    return (R, G, B)


class c_grad:
    """
    Making color gradients between arbitrary pairs of RGB colors smoothly transition
    from one color to another tends to look subtly wrong usually getting
    super dark or washing out halfway between two colors.

    For example:
    value         | color
    (255, 0, 0)   | bright red
    (127, 127, 0) | dull yellow
    (0, 255, 0)   | bright green

    On the way from bright red to bright green we go through dull yellow surely
    we want to go through bright yellow?

    In HSV the same gradient works like this:
    (0, 1, 1)   | bright red
    (60, 1, 1)  | bright yellow
    (120, 1, 1) | bright green

    You get the same progression of color, but we don't darken the yellow
    for no reason.

    HSV colors are related to each other more similarly to the way the eye naturally
    perceive the relationship between colors so it makes fewer gradients that
    look wrong.
    """

    def __init__(self, rgb_color_1, rgb_color_2, minimum, maximum):
        self.set_colors(rgb_color_1, rgb_color_2)
        self.set_domain(minimum, maximum)

    def set_colors(self, c1, c2):
        """
        Sets the colors for the the gradiant
        Args:
            c1: The RGB tuple for the minimum value
            c2: The RGB color for the maximum value
        """
        self.hsv1 = list(rgb_to_hsv(*c1))
        self.hsv2 = list(rgb_to_hsv(*c2))
        logging.info('hsv {} -> {}'.format(self.hsv1, self.hsv2))

    def set_domain(self, minimum, maximum):
        assert minimum < maximum, f"Provide a valid domain {minimum} !< {maximum}"
        self.min_v = minimum
        self.max_v = maximum
        self.mag = maximum - minimum

    def get_val(self, val):
        """
        hsv interpolation taken from
        https://www.alanzucconi.com/2016/01/06/colour-interpolation/2/
        """
        assert val >= self.min_v and val <= self.max_v, f"\
            value: {val} outside domain ({self.min_v}, {self.max_v})"

        t = (val - self.min_v) / self.mag
        dH = self.hsv2[0] - self.hsv1[0]
        dS = self.hsv2[1] - self.hsv1[1]
        dV = self.hsv2[2] - self.hsv1[2]
        logger.debug(f'dH: {dH} dS: {dS} dV: {dV} t: {t}')

        if dH > 180:  # 180 deg
            dH = dH - 360
            t = 1 - t
            logger.debug(f' dH is now {dH} t is now {t}')

        h = self.hsv1[0] + t * dH
        s = self.hsv1[1] + t * dS
        v = self.hsv1[2] + t * dV
        return hsv_to_rgb(h, s, v)


def set_ANSI_bg_color(astr, rgb_tuple):
    """
    Adds ANSI escape codes to astr to give it the background color from rgb_tuple
    """
    start_block = "\033[48;2;{};{};{}m".format(*rgb_tuple)
    end_block = "\033[0m"
    if not sys.stdout.isatty():
        logging.debug('Color mode not supported')
        return astr

    return start_block + astr + end_block


def set_ANSI_fg_color(astr, rgb_tuple):
    """
    Adds ANSI escape codes to astr to give it the foreground color from rgb_tuple
    """
    start_block = "\033[38;2;{};{};{}m".format(*rgb_tuple)
    end_block = "\033[0m"
    if not sys.stdout.isatty():
        logging.debug('Color mode not supported')
        return astr

    return start_block + astr + end_block
