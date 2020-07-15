"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5


说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
from tag_listnode import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        count = 1
        res = cur = ListNode(-1)
        temp_head_next = None
        temp = temp_ = head
        while head:
            if count == k:
                count = 1
                # 记录当前head结点
                temp_head_next = head.next

                # 交换
                after_head, after_tail = self.reverse(temp, head)
                cur.next = after_head
                cur = after_tail
                temp = temp_ = head = temp_head_next
                continue

            head = head.next
            temp_ = temp_.next
            count += 1
        if 1 < count <= k:
            cur.next = temp_head_next

        return res.next

    def reverse(self, head: ListNode, tail: ListNode):
        cur = head
        new_head = None
        while head != tail:
            temp = head.next
            head.next = new_head

            new_head = head
            head = temp
        head.next = new_head

        a_head = head
        a_tail = cur

        return a_head, a_tail


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)
# l1.next.next.next.next.next = ListNode(6)

Solution().reverseKGroup(l1, 3)
