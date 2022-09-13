class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []

        used = [0] * n

        def backtrack(nums, used, path):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtrack(nums, used, path)
                    path.pop()
                    used[i] = 0

        backtrack(sorted(nums), used, [])
        return ans
    