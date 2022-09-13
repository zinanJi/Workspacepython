# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy

        """
        待理逻辑
        # 从哑结点开始，结果是
        # 1. node往前移动（node = node1[node.next]）
        # 2. 第二个节点指回第一个节点 node2.next = node1
        # 3. 第一个节点指向第二个节点的下一个节点 node1.next = node2.next
        # 4. ...
        # 5. 第k个节点指回第k-1个节点 node2.next = node1
        # 6. 第k-1个节点指向第k个节点的下一个节点 node1.next = node2.next
        # 7. node指向第k个节点 node.next = node2
        # 为了不断链，则顺序应该是7-6-5-4-3-2-1
        """
        while True:
            tail = node
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            node1 = node.next
            for i in range(k - 1):
                # 循环内，变化的只有node2，node1的next指针，node2的next指针以及node的next指针
                # node1和node是不变的
                # 循环结束，node指向第k个节点，第1个节点指向k+1个节点，中间的链条反转
                node2 = node1.next
                node1.next = node2.next
                node2.next = node.next
                node.next = node2
            # node左移成为下一个k组的第0个节点
            node = node1
        return dummy.next
