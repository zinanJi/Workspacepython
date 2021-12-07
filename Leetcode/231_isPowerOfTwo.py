class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # n & (n - 1) = 0 那么 n 就是 2 的幂
        # n & (n - 1)的位运算技巧可以直接将 n 二进制表示的最低位 1 移除
        # n = 100000, n-1 = 011111 &一下就是000000
        # n = 110000, n-1 = 101111 &一下就是100000
        # return n > 0 and (n & (n - 1)) == 0

        # n & (-n) = n，那么 n 就是 2 的幂
        # 负数是按照补码规则在计算机中存储的
        # -n 的二进制表示为 n 的二进制表示的每一位取反再加上 1
        return n > 0 and (n & (-n)) == n
