class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 暴力算法超出时间限制
        # n = len(haystack)
        # needle_len = len(needle)
        # ans = -1
        # left = 0
        # while left < n - needle_len:
        #     if haystack[left] == needle[left]:
        #         for i in range(needle_len):
        #             if haystack[i] != needle[i]:
        #                 left += 1
        #                 break
        #             ans = left
        #             return ans
        # return ans

        # KMP算法
        # 维护next数组
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        next = self.getNext(m, needle)

        # next数组生成后，快慢指针重新以相同的指针回退方法(p=next[p])进行字符串匹配
        p = -1
        for j in range(n):
            while p >= 0 and needle[p + 1] != haystack[j]:
                p = next[p]
            if needle[p + 1] == haystack[j]:
                p += 1
            # 当慢指针长度达到模式串长度，说明找到了第一个符合要求的模式串
            if p == m - 1:
                return j - m + 1
        return -1

    # 构造next数组
    # 数组长度与模式串长度相同
    def getNext(self, m, needle):
        # 初始化
        next = ['' for i in range(m)]
        # 默认赋-1，理解为模式串的指针索引-1，同时赋作next的值，形成一个模式串索引与next数组索引的映射
        k = -1
        # 第一个字符不需要计算前后缀，next数组值=k
        next[0] = k
        # i 是快指针，k是会回退的慢指针，next[i]记录k值
        for i in range(1, len(needle)):
            # 当第二个以后的字符与模式串不匹配，则k回到next[k]指示的上一个最长前后缀的位置
            while k > -1 and needle[k + 1] != needle[i]:
                k = next[k]
            # 当第二个以后的字符与模式串字符匹配，则k指针和i指针一起移动
            if needle[k + 1] == needle[i]:
                k += 1
            # 无论k指针移不移动，i索引所在的next数组值都会更新
            next[i] = k
        return next
