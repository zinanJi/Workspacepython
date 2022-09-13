class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        # 只有1行或1列
        if numRows == 1 or numRows >= n:
            return s
        # 初始化字符串数组
        rows = ["" for _ in range(numRows)]
        # 设置方向变量，False向下，True向上
        down = False
        # 设置当前行变量
        row = 0
        for i in range(n):
            rows[row] += s[i]
            # 如果到了第0行或者最后一行，则调转方向
            if row == 0 or row == numRows - 1:
                down = not down
            # 继续走下一行
            row += 1 if down else -1
        ans = ""
        for i in range(numRows):
            ans += rows[i]
        return ans
