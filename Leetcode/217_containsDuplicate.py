import collections


class Solution:
    def containsDuplicate(self, nums):
        # 1.
        # return len(list(set(nums)))<len(nums)

        # 2.
        hash_map = collections.defaultdict(int)
        for num in nums:
            hash_map[num] += 1
            if hash_map[num] > 1:
                return True
        return False
