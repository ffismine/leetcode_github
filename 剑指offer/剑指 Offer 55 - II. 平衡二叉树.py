# -*- coding: utf-8 -*-
# Time   : 2020/8/10 13:21
# Author : Zhang Xie

"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""

# 左右递归遍历.
# 但是写的过程中，从顶到下和从下至顶，有点弄混了


from tag_tree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root_):
            if not root_:
                return 0
            left_depth = depth(root_.left)
            if left_depth == -1:
                return -1
            right_depth = depth(root_.right)
            if right_depth == -1:
                return -1
            return max(left_depth, right_depth) + 1 if abs(left_depth - right_depth) <= 1 else -1

        return depth(root) != -1


A = TreeNode(1)
A.left = TreeNode(2)
A.left.left = TreeNode(3)
A.left.left.left = TreeNode(4)
A.right = TreeNode(2)
A.right.right = TreeNode(3)
A.right.right.right = TreeNode(4)

print(Solution().isBalanced(A))
