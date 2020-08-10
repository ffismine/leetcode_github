# -*- coding: utf-8 -*-
# Time   : 2020/8/10 12:48
# Author : Zhang Xie

"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]
"""

# 基本上和32II类似，加个翻转而已


from typing import List

from tag_tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = [[root.val]]
        count = 0
        while queue:
            temp = []
            temp_res = []
            for x in queue:
                if x.left:
                    temp_res.append(x.left.val)
                    temp.append(x.left)
                if x.right:
                    temp_res.append(x.right.val)
                    temp.append(x.right)

            if count % 2 ==0:
                res.append(temp_res[::-1])
            else:
                res.append(temp_res)

            count += 1
            queue = temp

        res.pop()

        return res

