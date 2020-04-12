# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/4/11 11:04

"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2

给定的树 B：
   4 
  /
 1

返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
"""
'''
Solution是很多人提到的，但是解法2更加清晰易懂
Solution1 是通过树的深度遍历来找当前树是否和B根节点一样，如果一样，再去判断其他的是否一样。
个人推荐Solution1
'''
from tag_tree import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        # 判断A当前子树是否和B完全一样
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        if A and B:
            if recur(A, B):
                return True
            else:
                if self.isSubStructure(A.left, B):
                    return True
                else:
                    return self.isSubStructure(A.right, B)
        else:
            return False


class Solution1(object):
    def isSubStructure(self, A, B):
        result = False
        if A and B:  # A和B都不为空
            if A.val == B.val:
                result = self.isSubTree(A, B)  # 递归的判断他们各自左右节点的值是不是相同
            if not result:
                result = self.isSubStructure(A.left, B)  # 不相等则将树A的左子树与B进行比较
            if not result:
                result = self.isSubStructure(A.right, B)  # 不相等则将树A的右子树与B进行比较
        return result

    def isSubTree(self, root_A, root_B):
        if not root_B:  # 如果B为空,说明前面的节点都能一一对应上了,所以B是A的子树
            return True
        if not root_A:  # 如果A为空,则说明B不是他的子树
            return False
        if root_A.val != root_B.val:  # 节点值不相等,说明也不是
            return False
        # 判断左右子树是否符合
        return self.isSubTree(root_A.left, root_B.left) and self.isSubTree(root_A.right, root_B.right)



# A = [3,4,5,1,2], B = [4,1]
A = TreeNode(3)
A.left = TreeNode(4)
A.right = TreeNode(5)
A.right.left = TreeNode(1)
A.left.right = TreeNode(2)

B = TreeNode(5)
B.left = TreeNode(1)

Solution().isSubStructure(A, B)
Solution1().isSubStructure(A, B)