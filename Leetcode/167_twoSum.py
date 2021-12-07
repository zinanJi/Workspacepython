class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 非递减顺序排列
        # 固定一个数，二分查找
        
        # 双指针——初始时两个指针分别指向第一个元素位置和最后一个元素的位置
        low, high = 0, len(numbers) - 1
        while low <= high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))
