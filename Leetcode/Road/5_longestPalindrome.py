class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 状态转移方程：
        # 子串长度为1，dp[i][i] = True
        # 子串长度为2，且s[i]==s[j],即s[i]=s[i+1]
        # dp[i][j] = dp[i+1][j-1] and s[i]==s[j]

        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j]表示s[i...j]是否是回文串
        # 二维数组，i,j∈[0,n], 结构为n×n,值初始化为False
        dp = [[False] * n for _ in range(n)]
        # 将长度为1的子串初始化为True
        for i in range(n):
            dp[i][i] = True

        # 枚举的通常是所求解的值域范围
        # 枚举子串长度，目标子串的范围∈[2,n+1]
        for L in range(2, n + 1):
            # 枚举左边界
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # s[i] == s[i+1] 则dp[i][i+1] = True
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # 记录输出
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
