# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/4 18:26


"""
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


'''
思考：链表翻转问题经常遇到，重点在于具体过程先对哪个节点动刀子。
以1→2→3为例，翻转为321：1指向2→1为尾结点；2指向3→2指向1；3为尾结点→3指向2
如果直接令2指向1，那么3的地址就丢失了。
因此先来个变量指向3，然后2指向1，然后继续遍历。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode):
        new_head = None
        while head:
            # temp指向当前节点的下一个节点
            tmp = head.next
            # 然后将当前节点指向new_head
            head.next = new_head
            # 都前进一位
            new_head = head
            head = tmp
        return new_head


class Solution1:
    def reverseList(self, head: ListNode) :
        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return nextNode


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l2 = Solution().reverseList(l1)
print(l2.val, l2.next.val, l2.next.next.val, l2.next.next.next.val)

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l2 = Solution1().reverseList(l1)
print(l2.val, l2.next.val, l2.next.next.val, l2.next.next.next.val)
