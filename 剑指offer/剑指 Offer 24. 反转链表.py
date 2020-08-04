# -*- coding: utf-8 -*-
# Time    : 2020/8/4 10:41
# Author  : Zhang Xie

"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL 

限制：
0 <= 节点个数 <= 5000
"""

from tag_listnode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp

        return new_head


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

Solution().reverseList(l1)
