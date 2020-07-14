"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


'''
思考：其实最难的点在于，res - 1 - 2 - 3 变为 res - 2 - 1 - 3 ...   
这个过程需要一系列指针操作，因此需要辅助指针left_right和right_left的帮助


prev = right_left.next             # 记录2的后继
left_right.next = prev             # 将1指向2的后继 
right_left.next = left_right       # 将2指向1  
cur.next = right_left              # 将1的前驱指向2

其实这个过程23两步可以调换，但是调换会出现1指向2,2也指向1。因此上面就是最佳顺序


之后再记录新的前驱，即2,
以及记录新的12.即34
'''
from tag_listnode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        res = cur = ListNode(-1)
        while head and head.next:
            # 先在左，后在右
            left_right = head
            # 先在右，后在左
            right_left = head.next

            # 逆转1和2，并且头指针和尾指针弄好
            prev = right_left.next  # 记录尾指针
            left_right.next = prev
            right_left.next = left_right
            cur.next = right_left

            # 记录新的head
            cur = left_right
            head = prev

        return res.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

Solution().swapPairs(l1)
