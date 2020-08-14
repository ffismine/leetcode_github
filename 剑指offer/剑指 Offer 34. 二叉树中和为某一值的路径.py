# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/8/14 11:11

"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1


    A = TreeNode(5)
    A.left = TreeNode(4)
    A.right = TreeNode(8)
    A.left.left = TreeNode(11)
    A.right.right = TreeNode(4)
    A.right.left = TreeNode(13)
    A.left.left.left = TreeNode(7)
    A.left.left.right = TreeNode(2)
    A.right.right.left = TreeNode(5)
    A.right.right.right = TreeNode(1)

返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：
节点总数 <= 10000
"""

# 思考：
# 深度遍历，然后还剩0的时候，且叶子节点，就保存

# 要想写对还是不容易，要记住遍历所有的点，然后不符合回溯就行，不用提前结束
# 70 78行


from typing import List

from tag_tree import TreeNode


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res = []
        cur = []

        def helper(root, tag):
            if not root:
                return
            else:
                tag -= root.val
                cur.append(root.val)
                if tag == 0 and not root.left and not root.right:
                    res.append(cur[:])
                    cur.pop()
                    return

                helper(root.left, tag)
                helper(root.right, tag)
                cur.pop()

        helper(root, sum)

        return res


A = TreeNode(5)
A.left = TreeNode(4)
A.right = TreeNode(8)
A.left.left = TreeNode(11)
A.right.right = TreeNode(4)
A.right.left = TreeNode(9)
A.left.left.left = TreeNode(7)
A.left.left.right = TreeNode(2)
A.right.right.left = TreeNode(5)
A.right.right.right = TreeNode(1)

print(Solution().pathSum(A, 22))
