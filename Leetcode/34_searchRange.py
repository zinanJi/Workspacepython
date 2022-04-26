class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return [-1, -1]
        
        # 确定左边界
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        left = low if nums[low] == target else -1

        # 确定右边界
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = ((low + high) >> 1) + 1
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid

        right = high if nums[high] == target else -1

        return [left, right]
