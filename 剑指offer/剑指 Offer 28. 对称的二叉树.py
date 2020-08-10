# -*- coding: utf-8 -*-
# Time   : 2020/8/10 13:02
# Author : Zhang Xie


"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
"""

# 这题应该正常左右中和右左中遍历，一样，就完事了
from tag_tree import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        res1 = []
        res2 = []

        def digui1(root_):
            if not root_:
                res1.append("")
                return
            digui1(root_.left)
            digui1(root_.right)
            res1.append(root_.val)


        def digui2(root_):
            if not root_:
                res2.append("")
                return
            digui2(root_.right)
            digui2(root_.left)
            res2.append(root_.val)

        digui1(root)
        digui2(root)

        return res1 == res2


A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(2)
A.left.left = TreeNode(3)

A.right.right = TreeNode(3)

print(Solution().isSymmetric(A))