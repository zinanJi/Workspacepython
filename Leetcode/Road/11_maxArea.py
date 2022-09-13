class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1

        maxArea = 0

        while i < j:
            cur = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, cur)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
