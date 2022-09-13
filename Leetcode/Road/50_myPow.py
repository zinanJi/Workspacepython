class Solution(object):
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # 递归
        def quickMul(N):
            if N == 0:
                return 1
            #
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 迭代
        def quickMul(N):
            ans = 1.0
            x_contribute = x
            # 拆分指数N
            while N > 0:
                # 二进制最低位为1
                if N % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                # 舍弃二进制最低位
                N //= 2

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
