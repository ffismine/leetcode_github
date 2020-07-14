"""
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

示例 1：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

示例 2：
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
 
提示：
给定链表的结点数介于 1 和 100 之间。
"""
from tag_listnode import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        if head.next.next is None:
            return head if head.next is None or head.next is None else head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)

Solution().middleNode(l1)
