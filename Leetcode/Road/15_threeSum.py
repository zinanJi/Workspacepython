class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 标签:双指针

        n = len(nums)
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            # 当前值>0,后续不可能有三个数加和为0，直接返回结果
            if nums[i] > 0:
                return res
            # 元素与上一个重复，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 枚举元素i,另外两个数用左右指针处理
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 左指针往右去除重复项
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    # 右指针往左去除重复项
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    # 各自去除重复项后，再移动一次指针参与下一次枚举
                    L += 1
                    R -= 1
                # 不符合要求，三数和>0说明最大值过大，右指针左移
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                # 不符合要求，三数和<0说明最小值过小，左指针右移
                else:
                    L += 1
        return res
nums=[-1,0,1,2,-1,-4]
print(Solution().threeSum(nums=nums))