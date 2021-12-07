import collections


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 利用双端队列
        if not root:
            return []
        ans = []
        queue = collections.deque([root])
        f = True
        while queue:
            size = len(queue)
            tmp = collections.deque([])
            for _ in range(size):
                r = queue.popleft()
                if f:
                    tmp.append(r.val)
                else:
                    tmp.appendleft(r.val)

                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)

            f = not f
            ans.append(list(tmp))
        return ans
