import collections


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = collections.deque([root])
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                if i == size - 1:
                    ans.append(n.val)
        return ans
