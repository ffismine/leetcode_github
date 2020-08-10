# -*- coding: utf-8 -*-
# Time   : 2020/8/10 9:25
# Author : Zhang Xie

"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：
0 <= 链表长度 <= 1000
"""


# 我写的有点笨，其实如果l1或者l2没了，那么直接连上后续的就行

from tag_listnode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = cur = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                v1, v2 = l1.val, l2.val
                if v1 > v2:
                    cur.next = ListNode(l2.val)
                    cur = cur.next
                    l2 = l2.next
                    continue
                elif v1 < v2:
                    cur.next = ListNode(l1.val)
                    cur = cur.next
                    l1 = l1.next
                    continue
                else:
                    cur.next = ListNode(l1.val)
                    cur = cur.next
                    cur.next = ListNode(l2.val)
                    cur = cur.next
                    l1 = l1.next
                    l2 = l2.next
                    continue
            if l1:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
                continue

            if l2:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
                continue

        return res.next


l1 = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(4)

Solution().mergeTwoLists(l1, l2)
