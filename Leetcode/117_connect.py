import collections


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                n = q.popleft()
                if i < size - 1:
                    n.next = q[0]
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return root
