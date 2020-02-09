from draw_binary_tree import TreeNode



class MaxHeap:

    def __init__(self):
        self.data_array = []

    def move_up(self, idex):
        if idex == 0:
            return
        parent_idx = (idex - 1) // 2
        if self.data_array[idex] > self.data_array[parent_idx]:

            self.data_array[idex], self.data_array[parent_idx] = self.data_array[parent_idx], self.data_array[idex]
            self.move_up(parent_idx)
        else:
            print(f'value at idx {idex} is in its heap position {self.data_array[idex]}')
            return

    def move_around(self, idex):

        left_idx = (2 * idex) + 1
        right_idx = (2 * idex) + 2

        if left_idx > len(self.data_array) - 1:
            return

        if self.data_array[left_idx] is None:
            return

        if self.data_array[left_idx] > self.data_array[idex]:
            self.data_array[left_idx], self.data_array[idex] = self.data_array[idex], self.data_array[left_idx]
            self.move_around(left_idx)

        if right_idx > len(self.data_array) - 1:
            return

        if self.data_array[right_idx] is None:
            return

        if self.data_array[right_idx] > self.data_array[idex]:
            self.data_array[right_idx], self.data_array[idex] = self.data_array[idex], self.data_array[right_idx]
            self.move_around(right_idx)

    def insert(self, new_value):

        self.data_array.append(new_value)
        new_idx = len(self.data_array) - 1
        self.move_up(new_idx)

    def delete(self):
        output = self.data_array[0]
        self.data_array[0] = self.data_array[-1]
        self.data_array = self.data_array[:-1]

        self.move_around(0)
        return output


def translate_heap(aheap):

    def make_node(idx):
        left_idx = (2 * idx) + 1
        right_idx = (2 * idx) + 2

        if aheap.data_array[idx] is None:
            return None

        new_node = TreeNode(aheap.data_array[idx])

        if left_idx < len(aheap.data_array) - 1:
            new_node.left = make_node(left_idx)
        else:
            new_node.left = None

        if right_idx < len(aheap.data_array) - 1:
            new_node.right = make_node(right_idx)
        else:
            new_node.right = None
        return new_node

    root = make_node(0)
    return root


def draw_current_heap(some_heap):
    tr = translate_heap(some_heap)
    tr.display()


mh = MaxHeap()
for i in range(10):
    mh.insert(i)


draw_current_heap(mh)

ret = mh.delete()
print(ret)

draw_current_heap(mh)
ret = mh.delete()
print(ret)
draw_current_heap(mh)
ret = mh.delete()
print(ret)
draw_current_heap(mh)
ret = mh.delete()
print(ret)
draw_current_heap(mh)
ret = mh.delete()
print(ret)
draw_current_heap(mh)
ret = mh.delete()
print(ret)
draw_current_heap(mh)
