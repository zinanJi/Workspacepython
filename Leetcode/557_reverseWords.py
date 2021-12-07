class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # return " ".join(word[::-1] for word in s.split(" "))

        # return " ".join(s.split(" ")[::-1][::-1])

        low = 0
        newstr = list()
        for i, chr in enumerate(s):
            if chr == ' ':
                newstr.append(s[low:i][::-1])
                low = i + 1
        newstr.append(s[low:len(s)][::-1])
        return " ".join(word for word in newstr)


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
