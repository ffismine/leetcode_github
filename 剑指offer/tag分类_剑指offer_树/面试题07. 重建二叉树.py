# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/11 10:05

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出前序遍历 preorder = [3,9,20,15,7]  中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
 
限制：0 <= 节点个数 <= 5000
"""

# Definition for a binary tree node.
from tag_tree import TreeNode


class Solution(object):
    def buildTree(self, preorder, inorder):
        # 判断叶子节点
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])

        #查找当前子树的根节点在中序遍历的索引
        mid_index = inorder.index(preorder[0])

        # 递归，注意长度相等
        root.left = self.buildTree(preorder[1:mid_index+1], inorder[:mid_index])
        root.right = self.buildTree(preorder[mid_index+1:], inorder[mid_index+1:])

        return root



Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
