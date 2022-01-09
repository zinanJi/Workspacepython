import collections


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 1
        if not root:
            return 0
        queue = collections.deque(root)
        while queue:
            # 用size记录每轮队列的长度，就能记录每一层的节点数
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            depth += 1
        return depth
