class Solution(object):
    def findKthElement(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        # 两个数组的左边界
        index1 = 0
        index2 = 0

        while True:
            # 如果num1已经遍历到最后右边界，则直接返回nums2中第k个数
            if index1 == m:
                return nums2[index2 + k - 1]
            # 如果num2已经遍历到最后右边界，则直接返回nums1中第k个数
            if index2 == n:
                return nums1[index1 + k - 1]
            # 如果剩下要找的第k个数中k=1则直接返回两个数组中较小的左边界元素
            if k == 1:
                return min(nums1[index1], nums2[index2])
            # 二分查找的pivot索引，min操作防止数组越界
            newIndex1 = min(index1 + k / 2 - 1, m - 1)
            newIndex2 = min(index2 + k / 2 - 1, n - 1)
            pivot1 = nums1[newIndex1]
            pivot2 = nums2[newIndex2]
            # A[k/2-1]和B[k/2-1]较小者不会是要找的第k个元素，减去那些个数并重设其左边界
            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 1:
            return self.findKthElement(nums1, nums2, (total_length + 1) / 2)
        else:
            return (self.findKthElement(nums1, nums2, total_length / 2) + self.findKthElement(nums1, nums2,
                                                                                              total_length / 2 + 1)) / 2.0
