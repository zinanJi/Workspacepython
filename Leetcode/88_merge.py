class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """
        nums1[m:] = nums2
        nums1.sort()
        """

        # 利用中间数组sorted存放
        i, j = 0, 0
        sorted = []
        while i < m or j < n:
            if i == m:
                sorted.append(nums2[j])
                j += 1
            elif j == n:
                sorted.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                sorted.append(nums1[i])
                i += 1
            else:
                sorted.append(nums2[j])
                j += 1
        nums1[:] = sorted
        