"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

限制：
0 <= 链表长度 <= 10000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from tag_listnode import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        # new_head = None
        while head:
            # temp = head.next
            # head.next = new_head
            # new_head = head
            # head = temp
            res.append(head.val)
            head = head.next

        return res[::-1]
