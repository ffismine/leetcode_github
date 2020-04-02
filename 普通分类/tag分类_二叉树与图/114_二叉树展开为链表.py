# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/23 23:00

"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6

将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

'''
思考：就地转换，其实就是将left置空，然后用right表示 next
投机取巧：前序遍历，存入列表，将列表相连（其实这不满足就地转换的条件）
真正办法：
寻找当前节点1左子树最右边的点4
将56接到4后面
1左子树转为右子树，左子树置空。
    1
     \
      2
     / \
    3   4
         \
          5
           \
            6

继续遍历右子树
'''

# Definition for a binary tree node.
from tag_tree import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 左子树为空，直接考虑下个点
        while root:
            # 记录左子树最右边节点
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 左子树最右边节点连上当前节点右子树
                pre.right = root.right
                root.right = root.left
                root.left = None
                # 下一个
            root = root.right


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right = TreeNode(5)
tree.right.right = TreeNode(6)

Solution().flatten(tree)