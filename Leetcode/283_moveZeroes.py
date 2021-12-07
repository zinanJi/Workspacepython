class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        # bubble
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if (nums[i] == 0):
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
        """

        # 双指针
        # 左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
# out = [1,3,12,0,0]
# 原数组操作
