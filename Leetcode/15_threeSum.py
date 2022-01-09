class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ans = list()
        for first in range(n):
            # 剪枝，固定的这个数需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            right = n - 1
            target = -nums[first]
            for left in range(first + 1, n):
                if left > first + 1 and nums[left] == nums[left - 1]:
                    continue
                while left < right and nums[left] + nums[right] > target:
                    right -= 1
                if left == right:
                    break
                if nums[left] + nums[right] == target:
                    ans.append([nums[first], nums[left], nums[right]])

        return ans
