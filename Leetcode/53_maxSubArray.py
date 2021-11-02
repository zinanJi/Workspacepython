import sys


class Solution(object):
    """
    分治法
    
    def maxSubSum(self, A, left, right):
        if left == right:
            return A[left]
        center = int((left + right) / 2)
        leftSum = self.maxSubSum(A, left, center)
        rightSum = self.maxSubSum(A, center + 1, right)

        leftCrossMax = -sys.maxsize - 1
        leftCrossSum = 0
        for i in range(center, left - 1, -1):
            leftCrossSum += A[i]
            leftCrossMax = max(leftCrossSum, leftCrossMax)

        rightCrossMax = -sys.maxsize - 1
        rightCrossSum = 0
        for i in range(center + 1, right + 1):
            rightCrossSum += A[i]
            rightCrossMax = max(rightCrossSum, rightCrossMax)

        crossSum = leftCrossMax + rightCrossMax
        result = max(leftSum, rightSum, crossSum)
        return result

    def maxSubArray(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        return (self.maxSubSum(nums, 0, len(nums) - 1))
    """

    # 动态规划
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        c = [0 for _ in range(len(nums))]
        c[0] = nums[0]
        for i in range(1, len(nums)):
            c[i] = max(c[i-1]+nums[i],nums[i])
        return max(c)
