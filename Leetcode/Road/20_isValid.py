class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 标签：栈
        # python的list内置了栈

        # 左右括号一一对应，用哈希表表示关系
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # 特殊判定
        if len(s) % 2 == 1:
            return False

        stack = list()

        for char in s:
            # 当前字符为右括号
            if char in pairs:
                # 栈空或者栈顶不是对应的左括号，则不符合要求
                if not stack or stack[-1] != pairs[char]:
                    return False
                # 栈顶左括号已找到对应右括号，弹出
                stack.pop()
            # 当前字符为左括号
            else:
                stack.append(char)
        # 最后栈为空则说明字符串处理完毕后没有无法匹配的括号，字符串符合要求
        return not stack
s="(]"
print(Solution().isValid(s))