class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 标签:动态规划，回溯
        if n <= 0:
            return []

        ans = []

        def backtrack(paths, left, right):
            if left > n or right > left:
                return
            if len(paths) == n * 2:
                ans.append(paths)
                return
            backtrack(paths + "(", left + 1, right)
            backtrack(paths + ")", left, right + 1)

        backtrack('', 0, 0)
        return ans


n = 3
print(Solution().generateParenthesis(n))
