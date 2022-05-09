class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

        return []

    def twoSum2(self, nums, target):
        n = len(nums)
        hashtable = dict()
        for i in range(n):
            if target - nums[i] in hashtable:
                return [hashtable[target - nums[i]], i]
            hashtable[nums[i]] = i
        return []
