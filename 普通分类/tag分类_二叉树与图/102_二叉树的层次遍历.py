"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List
from tag_tree import TreeNode
from tree_A import treeA


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.pop(0)
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res


# DFS
class Solution1:
    def level(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level + 1, res)
        if root.right:
            self.level(root.right, level + 1, res)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.level(root, 0, res)
        return res


Solution().levelOrder(treeA())
