# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/12 19:10

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。
假设输入的数组的任意两个数字都互不相同。

 
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true
"""

# 后序遍历，有特殊属性
# 从后往前遍历，先大后小，如果一直维持这个属性，就是对的

# 太难了，写一个小时 不会，后续复习吧

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True


print(Solution().verifyPostorder([4, 8, 6, 12, 16, 14, 10]))
