class Solution(object):
    # 快速排序
    # 堆排序
    def findKthLargest(self,nums,k):

        n = len(nums)
        return nums[n-k]

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums,k))
