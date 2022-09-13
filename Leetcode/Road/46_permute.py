class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯
        # 假设我们已经填到第first 个位置，那么nums 数组中[0,first−1] 是已填过的数的集合，[first,n−1] 是待填的数的集合。
        #
        n = len(nums)

        ans = []

        def backtrack(first=0):
            if first == n:
                ans.append(nums[:])
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return ans

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯
        # 使用标记数组used记录选择，path记录路径
        n = len(nums)
        used = [0] * n
        ans = []

        def backtrack(nums, used, path):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = 1
                    backtrack(nums, used, path)
                    path.pop()
                    used[i] = 0

        backtrack(nums, used, [])
        return ans
nums = [1,2,3]
print(Solution().permute1(nums))