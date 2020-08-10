# -*- coding: utf-8 -*-
# Time   : 2020/8/10 11:33
# Author : Zhang Xie

"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

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
 

提示：
节点总数 <= 1000
"""


# 思考：宽度优先遍历


from typing import List

from tag_tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = [[root.val]]
        while queue:
            temp = []
            res.append([])
            for x in queue:
                if x.left:
                    res[-1].append(x.left.val)
                    temp.append(x.left)
                if x.right:
                    res[-1].append(x.right.val)
                    temp.append(x.right)

            queue = temp

        res.pop()

        return res


A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
A.left.left = TreeNode(4)
A.right.right = TreeNode(5)

print(Solution().levelOrder(A))

