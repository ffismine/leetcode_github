"""
2. 两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# 思考：
# 需要注意几个点：1,位数不相等 2,进位 3,最后还要进位


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from tag_listnode import ListNode


class Solution:
    # 2. 两数相加
    # 示例：
    # 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    # 输出：7 -> 0 -> 8
    # 原因：342 + 465 = 807

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = cur = ListNode(-1)
        ten = 0
        one = 0
        v = 0
        while l1 or l2:
            va1 = l1.val if l1 else 0
            va2 = l2.val if l2 else 0
            v = va1 + va2 + ten
            ten = v // 10
            one = v % 10

            cur.next = ListNode(one)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            cur = cur.next
            if ten != 0:
                cur.next = ListNode(ten)
        return res.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

Solution().addTwoNumbers(l1, l2)
