# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
import matplotlib.pyplot as plt

class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []


    def sort_init(self, N):

        """initialize the data structure

        """

        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')


        self.id = [random.randint(0, N - 1) for i in range(N)]


    def get_id(self):
        """initialize the data structure

        """

        return self.id


    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx in range(len(self.id)):
            min = i_idx

            for j_idx in range(i_idx+1, len(self.id)):

                if self.id[j_idx] < self.id[min]:
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp


        return self.id

    def insertion_sort(self):
        """"Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """
        for i in range(1, len(self.id)):
            key = self.id[i]
            j = i - 1
            while j >= 0 and key < self.id[j]:
                self.id[j + 1] = self.id[j]
                j -= 1
                self.id[j+1] = key

        return self.id




    @property
    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """
        h = 1
        while h < len(self.id)/2:
            h = 2 * h + 1
        while h >= 1:
            k = int(h)
            for i in range(k, len(self.id)):
                for j in range(i, k-1, -k):
                    if self.id[j] < self.id[j-k]:
                        key = self.id[j]
                        self.id[j] = self.id[j-k]
                        self.id[j-k] = key
                    else:
                        break
            h = h/2

        return self.id

    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """
        n = len(self.id)
        for k in range(int(n/2),0,-1):
            self.sink(k, n)
        k = n
        while k > 1:
            temp = self.id[0]
            self.id[0] = self.id[k-1]
            self.id[k-1] = temp
            k -= 1
            self.sink(1, k)
        return self.id

    def sink(self, k, n):
        while 2*k <= n:
            j = int(2*k)
            if j < n and self.id[j-1] < self.id[j]:
                j += 1

            if not self.id[k-1] < self.id[j-1]:
                break

            temp = self.id[k-1]
            self.id[k-1] = self.id[j-1]
            self.id[j-1] = temp
            k = j


    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        n = len(self.id)
        aux = [None] * len(self.id)
        self.sorting_function(aux, 0, n-1)

        return self.id

    def sorting_function(self, aux, lo, hi):
        if hi <= lo:
            return
        mid = int(lo + ((hi - lo) / 2))
        self.sorting_function(aux, lo, mid)
        self.sorting_function(aux, mid + 1, hi)
        self.merge(aux, lo, mid, hi)

    def merge(self, aux, lo, mid, hi):
        for k in range(lo, hi + 1):
            aux[k] = self.id[k]
            i = lo
            j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                self.id[k] = aux[j]
                j +=1
            elif j > hi:
                self.id[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                self.id[k] = aux[j]
                j += 1
            else:
                self.id[k] = aux[i]
                i += 1

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """

        self.sort(0, len(self.id)-1)
        return self.id

    def partition(self,lo, hi):
        i = lo
        j = hi +1
        v=self.id[lo]
        while True:
            i+=1
            while self.id[i]<v:
                if i==hi: break
                else: i+=1
            j-=1

            while v<self.id[j]:
                if j==lo: break
                else: j-=1
            if i >= j:
                break
            temp = self.id[i]
            self.id[i] = self.id[j]
            self.id[j] = temp
        temp = self.id[lo]
        self.id[lo] = self.id[j]
        self.id[j] = temp
        return j

    def sort(self, lo, hi):
        if hi <= lo:
            return
        j = self.partition(lo, hi)
        self.sort(lo, j-1)
        self.sort(j+1, hi)

if __name__ == "__main__":
    # iteration
    set_szs = [10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5,10 ** 6]
    timing = []
    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = Sorting()
        inodes.sort_init(set_sz)
        t0 = time.time()

        inodes.quick_sort()

        t1 = time.time()
        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

       # plot also python's sorted() function to see how well you do

    plt.plot(set_szs, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()
