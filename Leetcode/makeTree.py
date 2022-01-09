# https://blog.csdn.net/Mr_111000/article/details/119680459
# Definition for a Node.
import collections


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    #  采用了null占位，输入序列可以看做是对一棵完全二叉树的层序遍历
    def generate(list: list):
        q = []
        if not list:
            return
        # 将列表list的第一个元素（即对应树的根节点）移除队列，生成根节点 root 并入队 q
        root = Node(val=list.pop(0))
        q.append(root)
        while q:
            # q的第一个元素出队，记为节点 t
            t = q.pop(0)
            #  将列表list的下两个元素（若存在）移出队列 list，并生成节点 t 的左叶子节点和右叶子结点，将对应叶子节点入队 q
            if list:
                if list[0] != 'null':
                    t.left = Node(val=list.pop(0))
                    q.append(t.left)
                else:
                    list.pop(0)
            if list:
                if list[0] != 'null':
                    t.right = Node(val=list.pop(0))
                    q.append(t.right)
                else:
                    list.pop(0)
        return root

    def levelOrderPrintNext(root):
        if not root:
            return []
        res = []
        q = collections.deque([root])
        while q:
            size = len(q)
            while size > 0:
                n = q.popleft()
                res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                size -= 1
            res.append('#')
        return res
