class Solution(object):

    def recurse(self, array):
        if len(array) <= 2:
            return array
        return self.recurse(array[::2]) + self.recurse(array[1::2])

    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return self.recurse([x for x in range(1, n + 1)])

    def beautifulArray_bin_sort(self, n):
        return sorted(range(1, n + 1), key=lambda x: bin(x)[:1:-1])

    



