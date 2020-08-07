# -*- coding: utf-8 -*-
# Time   : 2020/8/6 11:07
# Author : Zhang Xie

"""
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

"""
# 这题的关键在于，求一棵二叉搜索树的第k大，注意大
# 树总节点个数我们不知道，但是二叉搜索树的中序遍历是递增的，因此右中左就是递减的，因此到了第k个 就可以停下来了


from tag_tree import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []

        def rmlTree(root_):
            if not root_:
                return
            rmlTree(root_.right)
            res.append(root_.val)
            rmlTree(root_.left)

        rmlTree(root)

        return res[k - 1]


A = TreeNode(5)
A.left = TreeNode(3)
A.right = TreeNode(6)
A.left.left = TreeNode(2)
A.left.right = TreeNode(4)

Solution().kthLargest(A, 3)
