import logging


class AsciiCanvas(object):

    def __init__(self, width, height, bg_fill_symbol='.'):

        self.log = logging.getLogger('canvas')
        self.log.setLevel(logging.DEBUG)

        # if width % 2 == 0:
        #     self.log.debug("enforcing odd cavas width")
        #     width += 1

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

    def draw(self):

        output_str = ''
        for row in self.canvas:
            output_str += ''.join(row) + '\n'
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

        word_size = len(word)
        if word_size % 2 == 0:
            self.log.debug('Words of even length make me sad.')
            w_start = x - word_size // 2
        else:
            w_start = x - 1 - word_size // 2

        for word_char in word:
            self.add_symbol_at(word_char, w_start, y)
            w_start += 1
