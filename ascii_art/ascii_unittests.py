import unittest
from ascii_art_utils import AsciiCanvas


class TestAsciiCanvas(unittest.TestCase):

    def setUp(self):
        self.tc = AsciiCanvas(4, 2, '.')

    def test_draw(self):
        self.tc.add_symbol_at('#', 0, 0)
        self.tc.add_symbol_at('#', 3, 1)
        res = self.tc.draw()
        expected = "#...\n...#\n"
        self.assertEqual(res, expected)

    def test_add_word(self):
        self.tc.add_word_at("test", 0, 1)
        res = self.tc.draw()
        expected = "....\ntest\n"
        self.assertEqual(res, expected)

    def test_straight_line_symbol(self):

        self.assertEqual(self.tc.straight_line_symbol(1, 1, 1, 5), '|')

        self.assertEqual(self.tc.straight_line_symbol(1, 2, 5, 2), '-')

        self.assertEqual(self.tc.straight_line_symbol(1, 1, 2, 2), '\\')
        self.assertEqual(self.tc.straight_line_symbol(2, 2, 1, 1), '\\')
        self.assertEqual(self.tc.straight_line_symbol(1, 2, 2, 1), '/')
        self.assertEqual(self.tc.straight_line_symbol(2, 1, 1, 2), '/')


if __name__ == "__main__":

    unittest.main()
