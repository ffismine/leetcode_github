"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。
"""

# 思考：双指针，先移动n次，后指针跟上，然后删除后指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from tag_listnode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return
        res = slow = head
        k = 0
        while head:
            head = head.next
            if not head:
                break
            k += 1
            if k > n:
                slow = slow.next

        # 这一步剔除了去除开头的那种情况，如果链表长度可以提前获取，那么就不用写这么后面了
        if n > k:
            return res.next

        slow.next = slow.next.next

        return res


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(7)
l1.next.next.next.next = ListNode(9)

Solution().removeNthFromEnd(l1, 5)
