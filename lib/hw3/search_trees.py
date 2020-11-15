import time
import random


class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):

        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx + 1
        return False

    def bsearch(self, val):
        low = 0
        high = len(self.array) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if self.array[mid] < val:
                low = mid + 1
            elif self.array[mid] > val:
                high = mid - 1
            else:
                return mid
        return False


class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val):
        if (self.root is None):
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current.val == val:
            current.val = val
        elif current.val > val:
            if current.left is None:
                current.left = BST_Node(val)
            else:
                self.insertNode(current.left, val)
        elif current.val < val:
            if current.right is None:
                current.right = BST_Node(val)
            else:
                self.insertNode(current.right, val)

    def bsearch(self, val):
        if self.root is None:
            return False
        else:
            return self.searchNode(self.root, val)

    def searchNode(self, current, val):
        if current is None:
            return False
        elif current.val == val:
            return current
        elif current.val > val:
            return self.searchNode(current.left, val)
        else:
            return self.searchNode(current.right, val)

    def delete(self, val):
        if self.bsearch(val) == False:
            return False
        else:
            current = self.bsearch(val)
            if current.left is None:
                temp = current
                current = current.right
                temp = None
                return True
            elif current.right is None:
                temp = current
                current = current.left
                temp = None
                return True
            else:
                temp = self.minValueNode(current.right)
                self.delete(temp)
                current.val = temp
                return True

    def minValueNode(self, current):

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current.val


class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color


RED = True
BLACK = False


class RBBST:
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):
        if current is None:
            return False
        return current.color == RED

    def rotate_left(self, current):
        temp = current.right
        current.right = temp.left
        temp.left = current
        temp.color = current.color
        current.color = RED
        return temp

    def rotate_right(self, current):
        temp = current.left
        current.left = temp.right
        temp.right = current
        temp.color = current.color
        current.color = RED
        return temp

    def flip_colors(self, current):
        current.color = RED
        current.left.color = BLACK
        current.right.color = BLACK

    def insert(self, val):
        if (self.root is None):
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current is None:
            return RBBST_Node(val, RED)
        if current.val > val:
            current.left = self.insertNode(current.left, val)
        elif current.val < val:
            current.right = self.insertNode(current.right, val)
        else:
            current.val = val
        if self.is_red(current.right) and not self.is_red(current.left):
            if current == self.root:
                self.root = self.rotate_left(current)
            else:
                current = self.rotate_left(current)
        elif self.is_red(current.left) and self.is_red(current.left.left):
            if current == self.root:
                self.root = self.rotate_left(current)
            else:
                current = self.rotate_right(current)
        if self.is_red(current.left) and self.is_red(current.right):
            self.flip_colors(current)
        return current

    def bsearch(self, val):
        if self.root is None:
            return False
        else:
            return self.searchNode(self.root, val)

    def searchNode(self, current, val):
        if current is None:
            return False
        elif current.val == val:
            return current
        elif current.val > val:
            return self.searchNode(current.left, val)
        elif current.val < val:
            return self.searchNode(current.right, val)


if __name__ == "__main__":

    set_sz = 10
    tut = BST()

    vals = random.sample(range(1, 100), set_sz)

    for idx in range(set_sz - 1):
        tut.insert(vals[idx])

    print(tut.bsearch(vals[1]))
    print(tut.bsearch(11))

    tut_rb = RBBST()

    for idx in range(set_sz - 1):
        tut_rb.insert(vals[idx])

    print(tut.bsearch(vals[1]))
    print(tut.bsearch(11))