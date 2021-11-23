class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))
        """

        # 将原数组下标为 i 的元素放至新数组下标为 (i+k)mod n 的位置，最后将新数组拷贝至原数组
        n = len(nums)
        res = list(nums)
        for i, num in enumerate(nums):
            res[(i + k) % n] = num
            print((i + k) % n)
        for i in range(n):
            nums[i] = res[i]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
