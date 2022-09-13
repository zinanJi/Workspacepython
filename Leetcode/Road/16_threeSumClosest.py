class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        nums.sort()
        ans = 10 ** 7
        for i in range(n):
            # 元素与上一个重复，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 枚举元素i时另外两个数用左右指针处理
            L = i + 1
            R = n - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if s == target:
                    return target
                # 更新绝对值更小的答案
                if abs(s - target) < abs(ans - target):
                    ans = s
                # 左指针往右去除重复项
                while L < R and nums[L] == nums[L + 1]:
                    L += 1
                # 右指针往左去除重复项
                while L < R and nums[R] == nums[R - 1]:
                    R -= 1
                # 各自去除重复项后，再根据当前值与目标值的大小关系移动一次指针参与下一次枚举
                if s < target:
                    L += 1
                else:
                    R -= 1
        return ans
