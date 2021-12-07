import collections


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 统计 s1 中每个字符出现的次数
        counter1 = collections.Counter(s1)

        left = 0
        right = len(s1) - 1
        N = len(s2)
        # 统计s2的窗口[left,right-1]中元素出现的个数
        counter2 = collections.Counter(s2[0:right])

        while right < N:
            counter2[s2[right]] += 1
            if counter1 == counter2:
                return True
            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            left += 1
            right += 1
        return False


s1 = "hello"
s2 = "ooolleoooleh"
print(Solution().checkInclusion(s1, s2))
