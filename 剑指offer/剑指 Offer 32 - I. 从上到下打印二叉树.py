# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/12 17:13

"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。


例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000
"""

# 思考：老题目了，层次遍历

from typing import List

from definition.tag_tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        trees = [root]

        while trees:
            temp = []

            for t in trees:
                res.append(t.val)
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)

            trees = temp

        return res
