import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        if not root:
            return []

        ans = []

        def dfs(index, r):
            # 假设ans是[[1],[2,3]]， index是3，就再插入一个空list放到ans中
            if len(ans) < index:
                ans.append([])
            ans[index - 1].append(r.val)
            if r.left:
                dfs(index + 1, r.left)
            if r.right:
                dfs(index + 1, r.right)

        dfs(1, root)
        return ans
        """

        if not root:
            return []
        ans = []
        queue = collections.deque([root])
        while queue:
            # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
            size = len(queue)
            tmp = []
            for _ in range(size):
                r = queue.popleft()
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            ans.append(tmp)
        return ans
