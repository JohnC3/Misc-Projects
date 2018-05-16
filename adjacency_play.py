from copy import deepcopy
from pprint import pprint

detecting_islands = [
    [0, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1],
]


def next_label():
    reps = 1
    index = 0
    label = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        if index == 24:
            index = 0
            reps += 1
        yield reps * label[index]
        index += 1


################# METHOD 1 SIMPLE PROPAGATION OF LABEL ########################
# Just go through twice and check all adjs


def label_propagation(M):

    nrow = len(M)
    ncol = len(M[0])

    label_map = {}

    cur_label = 0

    for r in range(nrow):
        for c in range(ncol):
            val = M[r][c]
            label = []
            if val == 0:
                continue
            # if c < ncol:
            llabel = label_map.get((r, c + 1), None)
            if llabel:
                label.extend(llabel)
            # if c > 0:
            rlabel = label_map.get((r, c - 1), None)
            if rlabel:
                label.extend(rlabel)
            # if r < nrow:
            blabel = label_map.get((r + 1, c), None)
            if blabel:
                label.extend(blabel)
            # if r > 0:
            tlabel = label_map.get((r - 1, c), None)
            if tlabel:
                label.extend(tlabel)
            # If no adjacent nodes are labled this one gets a new label
            if len(label) == 0:

                label = [cur_label]
                cur_label += 1
            label_map[(r, c)] = label
    return label_map


def label_cleanup(label_dict):
    cleaned = {}
    for k in label_dict:
        final_label = min(label_dict[k])
        cleaned[k] = final_label
    return cleaned


def apply_labels(M, label_dict):
    out = deepcopy(M)

    for rc in label_dict:
        r, c = rc
        print(r, c)
        L = label_dict[rc]
        if type(L) == str:
            out[r][c] = label_dict[rc]
        elif type(L) == list:
            out[r][c] = ''.join(label_dict[rc])
    return out


# ex1L = label_propagation(detecting_islands)
#
# pprint(detecting_islands)
# pprint(ex1L)
#
# pprint(apply_labels(detecting_islands, ex1L))
