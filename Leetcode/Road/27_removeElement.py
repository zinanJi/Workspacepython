class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, 0
        # left表示已处理数组最后一个元素，已处理数组中不含val
        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        return left
