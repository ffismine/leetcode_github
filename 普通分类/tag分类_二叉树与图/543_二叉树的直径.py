"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 代码细节要注意，这题想完全做对，很难很难

from tag_tree import TreeNode


class Solution:
    def __init__(self):
        self.res = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)

        return self.res

    def depth(self, tree: TreeNode):
        if not tree:
            return 0

        left = self.depth(tree.left)
        right = self.depth(tree.right)

        self.res = max(self.res, left + right + 1)

        return max(left, right) + 1
