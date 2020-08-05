# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/5 23:05

"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""

from tag_tree import TreeNode


# 方法1：递归

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 方法2：层次遍历，每遍历一层+1

class Solution1:
    def maxDepth(self, root) -> int:
        res = 0
        queue = [root]

        while queue:
            stack = []
            for subtree in queue:
                if subtree.left:
                    stack.append(subtree.left)
                if subtree.right:
                    stack.append(subtree.right)
            queue = stack
            res += 1

        return res


A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
A.right.left = TreeNode(6)

Solution1().maxDepth(A)
