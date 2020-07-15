# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/11 22:54


"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

"""

'''
思考：
4个关键点：
1逆置前头节点的前驱(之后要指向逆置后的头节点)
2逆置前的头节点/逆置后尾节点(之后要指向逆置前的尾节点的后继)
3逆置前的尾节点/逆置后头节点(之后要指向逆置前的头节点的前驱)
4逆置前尾节点的后继(之后逆置后的尾节点要指向该节点)

首先head已知，就是2
1就是head向前移动m-1的位置的点
逆置n-m+1个节点

逆置结束之后，将逆置前头节点前驱指向逆置后头节点
将逆置前头节点指向逆置前尾结点后继

即前驱仍然是前驱，后继还是后继
'''
from tag_listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        if m == 1:
            before_head = head
            new_head = None
            for i in range(n - m + 1):
                temp = head.next
                head.next = new_head
                new_head = head
                head = temp  # 结束循环此时head为点4
                before_head.next = head
            return new_head

        else:
            # 最开始head是整个链表的head

            pre_head = None
            for i in range(m - 1):
                # 循环的最后一次记录下逆序前的头节点前驱,即点1
                if i == m - 2:
                    pre_head = head
                # 往后移动，找逆序前的头节点
                head = head.next
            # 点2，记录逆置前的头节点
            before_head = head

            # 开始逆序
            new_head = None
            for i in range(n - m + 1):
                temp = head.next
                head.next = new_head
                new_head = head
                head = temp  # 结束循环此时head为点4
            # 点2指向点4
            before_head.next = head
            # 点1指向点3
            pre_head.next = new_head

        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l2 = Solution().reverseBetween(l1, 1, 4)
print(l2)
