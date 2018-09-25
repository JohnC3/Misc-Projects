import logging
import sys

logger = logging.getLogger(__name__)


def set_bg_color(text, rgb):
    """
    Add ANSI escape codes to turn the background color of the text from rgb
    """
    start_block = "\033[48;2;{};{};{}m".format(*rgb)
    end_block = "\033[0m"
    if not sys.stdout.isatty():
        logger.debug('Color not supported!')
        return text

    return start_block + text + end_block


def set_fg_color(text, rgb):
    """
    Add ANSI escape codes to turn text to the rgb color
    """
    start_block = "\033[38;2;{};{};{}m".format(*rgb)
    end_block = "\033[0m"
    if not sys.stdout.isatty():
        logger.debug('Color not supported!')
        return text

    return start_block + text + end_block


class AsciiCanvas(object):

    def __init__(self, width, height, bg_fill_symbol='.'):

        self.log = logging.getLogger('canvas')
        self.log.setLevel(logging.DEBUG)
        self.width = width
        self.height = height
        self.bg_fill_symbol = bg_fill_symbol

        self.canvas = self.prep_canvas()

    def prep_canvas(self):
        canvas = []
        for _r in range(self.height):
            row = [self.bg_fill_symbol] * self.width
            canvas.append(row)
        return canvas

    def add_column(self, start=0, end=0):
        """
        Add a number of coloumns equal to start at the right side and end on
        the left coloumns containing the bg_fill_symbol to"""
        self.width = self.width + start + end

        if start > 0:
            for row in self.canvas:
                for _x in range(start):
                    row.insert(self.bg_fill_symbol, 0)
        if end > 0:
            for row in self.canvas:
                for _x in range(start):
                    row.append(self.bg_fill_symbol)

    def straight_line_symbol(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return 'o'
        if x1 == x2:
            return '|'
        if y1 == y2:
            return '-'
        if x1 < x2 and y1 < y2:
            return '\\'
        if x1 > x2 and y1 > y2:
            return '\\'
        if x1 > x2 and y1 < y2:
            return '/'
        if x1 < x2 and y1 > y2:
            return '/'

    def draw_line(self, x1, y1, x2, y2):
        height = abs(y1 - y2)
        delta_x = round((x2 - x1) / height)

        logger.info(f'height {height} delta_x {delta_x}')

        symbol = self.straight_line_symbol(x1, y1, x2, y2)
        x_i = x1
        for h in range(y1, y2):

            self.add_symbol_at(symbol, x_i, h)
            x_i += delta_x

    def draw(self):

        output_str = ''
        for row in self.canvas:
            output_str += ''.join(row) + '\r\n'
        return output_str

    def __str__(self):
        return self.draw()

    def __repr__(self):

        return """
        canvas object with
        width: {self.width}
        height: {self.height}
        fill:{self.bg_fill_symbol}
        """

    def add_symbol_at(self, symbol, x, y):

        row = self.canvas[y]
        row[x] = symbol

    def add_word_at(self, word, x, y):
        w_start = x
        for word_char in word:
            self.add_symbol_at(word_char, w_start, y)
            w_start += 1
