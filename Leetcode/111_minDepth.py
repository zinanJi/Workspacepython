import collections


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        """
        minDepth = 0
        q = collections.deque([root])
        while q:
            size = len(q)
            while size > 0:
                node = q.popleft()
                if node.left or node.right:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    size -= 1
                else:
                    break

            if size > 0:
                break
            minDepth += 1
        return minDepth
        """
        # deque 可以存二维向量，思想是在记录节点的时候同时记录节点所在层数
        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))

        return 0
