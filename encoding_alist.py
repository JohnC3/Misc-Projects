

class bNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


tt = bNode(1)

n1 = bNode(3)
n2 = bNode(4)
tt.left = n1
tt.right = n2
n3 = bNode(6)
n4 = bNode(7)

n1.left = n3
n1.right = n4

n5 = bNode(8)
n2.left = n5

serialized_array = []
"""
        1
      /    \
    3       4
   / \     / \
  6   7   8  N
 /\  / \ / \
N N  N N N  N

[1, 3, 6, None, None, 7, None, None, 4, 8, None, None, None]
"""
def serialize(root):

    # Do inorder traversal

    if root is None:
        return None

    if root.val is None:
        return None

    serialized_array.append(root.val)

    if root.left is None:
        serialized_array.append(None)
    else:
        serialize(root.left)

    if root.right is None:
        serialized_array.append(None)
    else:
        serialize(root.right)


serialize(tt)
print(serialized_array)

"""
        1
      /    \
    3       4
   / \     / \
  6   7   8  N
 /\  / \ / \
N N  N N N  N

[1, 3, 6, None, None, 7, None, None, 4, 8, None, None, None]
"""
#
# def deserialize(ser):
#
#     root = bNode(ser.pop(0))
#     prev = root
#
#     astack = []
#     while True:
#
#         cur = ser.pop(0)
#         # Fill down along the lefts unitull you hit a null
#
#
#         while cur is not None:
#             print('adding left', cur)
#             new = bNode(cur)
#             prev.left = new
#             astack.append(new)
#             prev = new
#             cur = ser.pop(0)
#         # Once you hit a null move backup one level and attempt to add a right node
#
#         cur = ser.pop(0)
#         while cur is None:
#             if len(astack) == 0:
#                 break
#             prev = astack.pop(-1)
#             prev.right = None
#             cur = ser.pop(0)
#         if cur is not None:
#             print('adding right', cur)
#             new = bNode(cur)
#             prev.right = new
#             prev = new
#         if len(ser) == 0:
#             break
#
#     return root


def deserialize(ser):

    root = bNode(ser.pop(0))
    prev = root
    astack = [root]
    while len(ser) > 0:


        cur = ser.pop(0)
        # Fill down along the lefts unitull you hit a null

        if cur is not None:
            new = bNode(cur)
            if prev.left is None:
                print('adding left', cur)
                prev.left = new
            else:
                print('adding right', cur)
                prev.right = new
            astack.append(new)
            # lvisited.append(id(new))
            prev = new

        else:
            if len(astack) == 0:
                break
            prev = astack.pop(-1)
            print('moving back', prev.val)


    return root


# deserialize(serialized_array)


def print_btree(tree_root):

    queue = [(tree_root, 0)]

    next = []
    lvl = 0
    outstr = []
    all_none = True
    while len(queue) > 0:

        if len(next) == 0:
            output = ['N'] * 2**lvl
            print('output at lvl {} is {}'.format(lvl, output))
            lvl += 1
        pNode, pdex = queue.pop(0)

        if pNode is None:
            next.append((None, 2 * pdex))
            next.append((None, 2 * pdex + 1))

        else:
            output[pdex] = pNode.val
            all_none = False
            next.append((pNode.left, 2 * pdex))
            next.append((pNode.right, 2 * pdex + 1))

        if len(queue) == 0:

            outstr.append(output)
            queue = next
            next = []
            if all_none:
                break
            all_none = True

    for out in outstr:
        print(out)
    # print(outstr)

print_btree(tt)

print_btree(deserialize(serialized_array))
