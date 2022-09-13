class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        # 原数字<新数字，说明已经处理了一半
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y // 10
