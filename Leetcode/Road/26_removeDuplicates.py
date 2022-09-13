class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        # 指向已去重的数组最后一个元素
        j = 0
        for i in range(1, n):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1


nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))
