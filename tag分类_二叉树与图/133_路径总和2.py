# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/22 16:25

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。\
说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

'''
首先从根节点开始先序遍历，push入栈，记录累加值（path_value）
以上树为例，遍历到7时，7为叶子结点，栈为 7 11 4 5
发现path_value与sum不相等，7出栈，回退到11，遍历2
path_value等于sum，然后栈数据整体保存
2出栈，4出栈，开始遍历右子树8，8入栈
13入栈，path_value与sum不相等，13出栈
4入栈，5入栈，path_value等于sum，栈数据整体保存
5出栈，1入栈，path_value与sum不相等，1出栈
8出栈，5出栈，栈空。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        ans = []
        # 栈
        path = []
        # 栈和
        path_value = 0
        self.helper(root, path_value, sum, path, ans)
        return ans

    def helper(self, tree_node, path_value, sum_, path, ans):
        if not tree_node:
            return
        path_value += tree_node.val
        # 压住栈
        path.append(tree_node.val)
        # 满足条件，将path添加至ans
        if path_value == sum_ and not tree_node.left and not tree_node.right:
            ans.append(path[:])
        self.helper(tree_node.left, path_value, sum_, path, ans)
        self.helper(tree_node.right, path_value, sum_, path, ans)
        # 遍历完成，减去，并且弹出
        path_value -= tree_node.val
        path.pop()


tree = TreeNode(5)
tree.left = TreeNode(4)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right = TreeNode(8)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.left = TreeNode(5)
tree.right.right.right = TreeNode(1)
print(Solution().pathSum(tree, 22))

