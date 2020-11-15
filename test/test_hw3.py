import copy
import random
from lib.hw3.search_trees import Array_Search
from lib.hw3.search_trees import BST
from lib.hw3.search_trees import RBBST


class Test_Search(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        print("\n#####  Start Function Tests   #####\n")

    def test_one(self):
        pass

    def test_two(self):
        expected = (1, 2, 3)
        actual = (1, 2, 3)
        assert expected == actual

    def test_sequential_search_0(self):

        # initialize testbed
        set_sz = 10
        vals = random.sample(range(1, 100), set_sz)
        op_under_test = Array_Search(vals)

        # python search result
        key = vals[9]
        expected = vals.index(key)

        actual = op_under_test.squential_search(key)

        assert expected == actual

    def test_array_search(self):
        vals = [1, 20, 32, 45, 46, 56, 58, 68, 90]
        to_test = Array_Search(vals)
        key = vals[5]
        not_found = False
        assert 5 == to_test.bsearch(key)
        assert not_found == to_test.bsearch(100)
        key = vals[6]
        assert 6 == to_test.bsearch(key)

    def test_BST(self):
        tree = BST()
        to_insert = [10, 20, 30, 5, 6, 15, 25, 35, 3, 8, 4, 1]
        for i in to_insert:
            tree.insert(i)

        not_found = False
        deleted = True

        assert tree.bsearch(5).val == 5
        assert not_found == tree.bsearch(100)
        assert not_found == tree.bsearch(34)
        assert not_found == tree.bsearch(26)
        assert deleted == tree.delete(5)
        assert not_found == tree.bsearch(5)
        assert tree.bsearch(3).val == 3
        assert not_found == tree.delete(100)
        assert deleted == tree.delete(10)
        assert tree.bsearch(30).val == 30

    def test_rbtree(self):
        tree = RBBST()
        to_insert = [10, 20, 30, 5, 6, 15, 25, 35, 3, 8, 4, 1]
        for i in to_insert:
            tree.insert(i)
        red = True
        not_found = False
        assert 30 == tree.bsearch(30).val
        assert 5 == tree.bsearch(5).val
        assert red != tree.is_red(tree.bsearch(5))
        assert red == tree.is_red(tree.bsearch(1))
        assert red != tree.is_red(tree.bsearch(15))
        assert 25 == tree.bsearch(25).val
        assert not_found == tree.bsearch(2)
        assert not_found == tree.bsearch(12)



    def test_rbbst_0(self):

        # initialize testbed
        set_sz = 10
        op_under_test = RBBST()

        vals = random.sample(range(1, 100), set_sz)

        for idx in range(set_sz - 1):
            op_under_test.insert(vals[idx])

        # python search result
        key = vals[9]
        expected = vals.index(key)

        actual = op_under_test.bsearch(key).val

        assert expected == actual

        # initialize testbed
        op_under_test = BST()
        op_under_test.init_bst(10)

        expected = sorted(op_under_test.get_id())

        actual = op_under_test.bsearch()

        assert expected == actual