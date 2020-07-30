"""
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
"""
from tag_listnode import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        c1 = c2 = head
        count = 0
        while head and head.next:
            if count < k - 1:
                head = head.next
                c2 = c2.next
                count += 1
            else:
                head = head.next
                c2 = c2.next
                c1 = c1.next

        return c1


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(7)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(10)

Solution().getKthFromEnd(l1, 3)
