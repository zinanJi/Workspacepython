class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        rk, ans = -1, 0

        for i in range(n):
            if i != 0:
                # 左指针右移，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第i到rk个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

        