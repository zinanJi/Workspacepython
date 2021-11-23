class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        def fn(x):
            return x**2
        res = map(fn, nums)
        res.sort()
        return res
        """
        """
        return sorted(num * num for num in nums)
        """
        """
        # 指针指向0和n-1，每次选最大放数组末尾
        left, right = 0, len(nums) - 1
        ans = list(nums)
        for i in range(len(ans) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                ans[i] = nums[left]**2
                left += 1
            else:
                ans[i] = nums[right]**2
                right -= 1
        return ans
        """

        n = len(nums)
        negative = -1
        for i, num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break
        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(nums[j]**2)
                j += 1
            elif j == n:
                ans.append(nums[i]**2)
                i -= 1
            elif nums[i]**2 < nums[j]**2:
                ans.append(nums[i]**2)
                i -= 1
            else:
                ans.append(nums[j]**2)
                j += 1
        return ans
