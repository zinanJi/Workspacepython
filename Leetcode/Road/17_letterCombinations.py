class Solution(object):
    VALUE2SYMBOLS_MAP = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 哈希表 字符串 回溯
        # 当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
        if not digits:
            return list()
        # 回溯方法：
        # index记录回溯的选择，combination记录路径
        # eg中index=4时选择列表为空，index=len(digits),加空字符backtrack函数返回
        # 执行过程：
        # index=0 取第一个数字2 遍历2对应的字母abc，将a加入路径，index+1取下一个数字6,...,index+1取最后一个数字8,遍历tuv，
        # 加t,index+1=len(digits)选择列表为空，撤销选择pop出t,加u,...,加v,...
        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in Solution.VALUE2SYMBOLS_MAP[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


digits = "2658"
print(Solution().letterCombinations(digits))
