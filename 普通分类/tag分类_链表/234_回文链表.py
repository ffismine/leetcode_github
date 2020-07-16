"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
from tag_listnode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        # push
        cur = head 
        while cur:
            stack.append(cur)
            cur = cur.next
        # pop
        node1 = head
        while stack:
            node2 = stack.pop()
            if node1.val != node2.val:
                return False
            node1 = node1.next
            
        return True
