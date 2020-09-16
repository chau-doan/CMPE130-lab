# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression28765

import time
import random
import matplotlib.pyplot as plt

class UF(object):
    """Union Find class

    """

    def __init__(self):
        self.id = []
        self.sz = []

    def find(self, p):
        return self.id[p]

    def qf_init(self, N):
        """initialize the data structure

        """
        for x in range(N):
            self.id.append(x)
            self.sz.append(1)

    def qf_union(self, p, q):
        """Union operation for Quick-Find Algorithm.

        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)

        """
        id_p = self.find(p)
        if not self.qf_connected(p, q):
            for i in range(len(self.id) - 1):
                if self.id[i] == id_p:
                    self.id[i] = self.id[q]
        return 1

    def qf_connected(self, p, q):
        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected

        """
        if self.find(p) == self.find(q):
            return True
        else:
            return False
        # return self.id[p] == self.id[q]

    def qu_find(self, a):

        while a != self.id[a]:
            a = self.id[a]
        return a

    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.

         """
        root_p = self.qu_find(p)
        root_q = self.qu_find(q)
        if not self.qu_connected(p, q):
            self.id[root_p] = root_q
        return 1

    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected

        """
        if self.qu_find(p) == self.qu_find(q):
            return True
        else:
            return False

    def wqu_find(self, a):

        while a != self.id[a]:
            a = self.id[a]
        return a

    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.

         """
        root_p = self.qu_find(p)
        root_q = self.qu_find(q)
        if not self.qu_connected(p, q):
            self.sz[root_p] < self.sz[root_q]
            self.id[root_p] = root_q
            self.sz[root_q] += self.sz[root_p]

        else:
            self.sz[root_p] += self.sz[root_q]
            self.id[root_q] = root_p

        return 1

    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """
        if self.wqu_find(p) == self.wqu_find(q):
            return True
        else:
            return False

    def pqu_find(self, a):

        while a != self.id[a]:
            self.id[a] = self.id[self.id[a]]
            a = self.id[a]
        return a

    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """
        i = self.pqu_find(p)
        j = self.pqu_find(q)
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        return 1

    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        if self.pqu_find(p) == self.pqu_find(q):
            return True
        else:
            return False

    def wpqu_find(self, p):

        root = p
        while root != self.id[root]:
            root = self.id[root]
        while p != root:
            newp = self.id[p]
            self.id[p] = root
            p = newp
        return root

    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """
        root_p = self.wpqu_find(p)
        root_q = self.wpqu_find(q)
        if self.sz[root_p] < self.sz[root_q]:
            self.id[root_p] = root_q
            self.sz[root_q] += self.sz[root_p]
        else:
            self.id[root_q] = root_p
            self.sz[root_p] += self.sz[root_q]

        return 1

    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        if self.wpqu_find(p) == self.wpqu_find(q):
            return True
        else:
            return False


if __name__ == "__main__":

    # iteration
    set_szs = [10**1, 10**2, 10**3, 10**4]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.qf_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!

    plt.plot(set_szs, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('plot')
    plt.ylabel('some numbers')
    plt.show()


