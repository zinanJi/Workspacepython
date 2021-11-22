# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(v):
    return True


class Solution(object):
    def firstBadVersion(self, n, target):
        """
        :type n: int
        :rtype: int
        """

        low, high = 1, n
        while low < high:
            mid = (high + low) >> 1
            if isBadVersion(mid, target):
                high = mid
            else:
                low = mid + 1
        return low
