#!/bin/python3

from ascii_art_utils import AsciiCanvas, set_bg_color, set_fg_color


class tNode:

    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def toy_add(root):
    print('adding to ', root.v)
    right_child = tNode(root.v + '0')
    left_child = tNode(root.v + '1')

    root.right = right_child
    root.left = left_child

    return right_child, left_child


def example_tree(tree_size=20):

    root = tNode('R')
    num_nodes = 1
    nodes_to_extend = [root]
    while num_nodes < tree_size:

        next = nodes_to_extend.pop(0)
        right, left = toy_add(next)

        nodes_to_extend.append(right)
        nodes_to_extend.append(left)
        num_nodes += 2
        print(num_nodes)
    return root


def get_tree_depth(root):
    if root is None:
        return 0
    rdepth = get_tree_depth(root.right) + 1
    ldepth = get_tree_depth(root.right) + 1
    return max([rdepth, ldepth])


class DrawTree(object):

    def __init__(self, max_label_size=5, min_label_gap=2, rows_between=3):
        self.MLS = max_label_size
        self.mLG = min_label_gap
        self.RG = rows_between

    def add_node_to_canvas(self, AC, tree_node, x, y, available_area):

        next_available_area = available_area // 2
        text = tree_node.v

        # text = set_bg_color(text, (255, 255, 0))

        while len(text) < self.MLS - 1:
            text = '_' + text + '_'
        AC.add_word_at(text, x - len(text) // 2, y)
        next_y = y + self.RG
        if tree_node.left is not None:

            left_x = x + next_available_area // 2
            AC.draw_line(x + self.mLG, y + 1, left_x, next_y)
            self.add_node_to_canvas(AC, tree_node.left, left_x, next_y,
                                    next_available_area)

        if tree_node.right is not None:
            right_x = x - next_available_area // 2
            AC.draw_line(x - self.mLG, y + 1, right_x, next_y)
            self.add_node_to_canvas(AC, tree_node.right, right_x, next_y,
                                    next_available_area)

    def draw_tree(self, root):
        depth = get_tree_depth(root)
        width = (self.MLS + 3 * self.mLG) * 2 ** depth
        height = depth * self.RG
        AC = AsciiCanvas(width, height, '.')

        self.add_node_to_canvas(AC, root, width // 2, 0, AC.width)
        return AC


if __name__ == "__main__":
    ex_tree = example_tree(10)
    get_tree_depth(ex_tree)

    print(ex_tree)

    dt = DrawTree(rows_between=5)

    print(dt.draw_tree(ex_tree))
