import collections
import makeTree


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 层次遍历
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # 关键步骤：pop之后队列头部即为该层取出节点的下一个节点（最后为null？），赋值给node.next
                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        """
        if not root:
            return root

        # 从根节点开始
        leftmost = root

        while leftmost.left:
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            # 去下一层的最左的节点
            leftmost = leftmost.left
        return root
        """


list = [1, 2, 3, 4, 5, 'null', 7]
root = makeTree.Node.generate(list=list)
print(makeTree.Node.levelOrderPrintNext(Solution().connect(root)))
