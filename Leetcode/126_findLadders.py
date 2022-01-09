class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        # 最短=>广度优先
        # wordList每个单词作为一个顶点构成一个无向图
        # 基于该图，我们以 beginWord 为图的起点， 以endWord 为终点进行广度优先搜索，寻找 beginWord 到 endWord 的最短路径。
        # 要求输出所有的最短路径，因此我们需要记录遍历路径，然后通过「回溯算法（深度优先遍历）」得到所有的最短路径。

        # 从一个单词出发，修改每一位字符，将它修改成为 a 到 z 中的所有字符，看看修改以后是不是在题目中给出的单词列表中；

        # endWord 不在列表中
        if endWord not in set(wordList):
            return []
