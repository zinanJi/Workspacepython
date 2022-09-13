class Solution(object):
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # 二分查找官解
        # Z×Y≥X>(Z+1)×Y
        # 使用二分查找得到Z，找到最大的Z使得Z×Y≥X成立
        if dividend == 0:
            return 0
        if dividend == Solution.INT_MIN:
            if divisor == 1:
                return Solution.INT_MIN
            if divisor == -1:
                return Solution.INT_MAX

        if divisor == Solution.INT_MIN:
            if dividend == Solution.INT_MIN:
                return 1
            else:
                return 0

        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        # 快速乘
        def quickAdd(y, z, x):
            # x与y为负数，z为正数
            # z * y >= x?
            result, add = 0, y
            # 拆分因数z
            while z > 0:
                # &1操作二进制判断奇偶，二进制最后一位是否为1
                if (z & 1) == 1:
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    if add < x - add:
                        return False
                    add += add
                z >>= 1
            return True

        left, right, ans = 1, Solution.INT_MAX, 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                if mid == Solution.INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1
        return -ans if rev else ans
