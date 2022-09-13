class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # set集合内无重复元素，适合做该题的容器
        window = set()
        n = len(s)
        # 初始化窗口右边界与目标输出
        rk, ans = -1, 0
        for i in range(n):
            # 除了第一轮，每轮迭代先让左边界指针右移，具体操作为将set中的第i-1个元素移除
            if i != 0:
                window.remove(s[i - 1])
            # 右边界指针扫描到不重复元素加入到窗口，直至扫描到重复元素
            while rk + 1 < n and s[rk + 1] not in window:
                window.add(s[rk + 1])
                rk += 1
            # 扫描到重复元素退出迭代，得到当前不重复子串长度，对比目标输出
            ans = max(ans, rk - i + 1)
        return ans
