# -*- coding: utf-8 -*-
# Time   : 2020/8/5 10:08
# Author : Zhang Xie

"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
         4
       /   \
      2     7
     / \   / \
    1   3 6   9

镜像输出：
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

 
示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""

# 思考：递归交换子树 就完事了

from tag_tree import TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        def swapSubtree(root_):
            if root_:
                root_.left, root_.right = root_.right, root_.left

            if hasSubtree(root_.left):
                swapSubtree(root_.left)
            if hasSubtree(root_.right):
                swapSubtree(root_.right)

        def hasSubtree(tree):
            if not tree:
                return False
            return True if (tree.left or tree.right) else False

        swapSubtree(root)

        return root


# 第二方法，别人的，辅助栈
class Solution1:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
