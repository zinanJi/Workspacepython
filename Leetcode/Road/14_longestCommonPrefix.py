class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # 思路：按列纵向查找最长公共前缀，以第一个字符串strs[0]为基准，只需要比较最多从strs[0][0]到strs[0][length-1]就能找到
        length, count = len(str[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or str[j][i] != c for j in range(j, count)):
                return strs[0][:i]
        return strs[0]

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # 思路：按行横向查找最长公共前缀，
        prefix = strs[0]
        counts = len(strs)
        for i in range(1, counts):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
