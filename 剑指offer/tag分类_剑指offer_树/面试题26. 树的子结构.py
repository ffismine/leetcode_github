# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/11 11:04

"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2

给定的树 B：
   4 
  /
 1

返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
"""
from tag_tree import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        # 判断A当前子树是否和B完全一样
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        if A and B:
            if recur(A, B):
                return True
            else:
                if self.isSubStructure(A.left, B):
                    return True
                else:
                    return self.isSubStructure(A.right, B)
        else:
            return False


# A = [3,4,5,1,2], B = [4,1]
A = TreeNode(3)
A.left = TreeNode(4)
A.right = TreeNode(5)
A.left.left = TreeNode(1)
A.left.right = TreeNode(2)

B = TreeNode(4)
B.left = TreeNode(1)

Solution().isSubStructure(A, B)
