# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/3/22 17:04

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 
说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
"""

'''
所谓祖先，就是父节点及其父节点的父节点等等
最近公共祖先，就是离根最远或者说离节点最近一级的公共祖先，最坏情况便是根节点。
注意特殊情况是公共祖先可以是本身，
那么如果一个点已经是另一个点的祖先，那么很明显最近公共祖先就是祖先本身

思考：其实如果是公共祖先，那么从根节点，到最后的最近公共祖先，路径是全是公共祖先
其实就是求经过pq的路径，最后的共同点。
'''
from tag_tree import TreeNode


# Definition for a binary tree node.


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 存储路径的两个栈
        path_p = []
        path_q = []
        ans_p =[]
        ans_q = []
        # 栈和
        self.hasfound = False
        self.helper(root, p, path_p, ans_p)
        self.hasfound = False
        self.helper(root, q, path_q, ans_q)
        result = root.val
        for i in range(min(len(ans_p[0]),len(ans_q[0]))):
            if ans_p[0][i] == ans_q[0][i]:
                result = ans_p[0][i]
            else:
                break
        return result

    def helper(self, tree_node, node, path, ans):
        if not tree_node or self.hasfound == True:
            return
        # 压住栈
        path.append(tree_node.val)
        # 找到了node，返回路径
        if tree_node.val == node.val:
            ans.append(path[:])
            self.hasfound = True
        self.helper(tree_node.left, node, path, ans)
        self.helper(tree_node.right, node, path, ans)
        # 遍历完成，减去，并且弹出
        path.pop()


tree = TreeNode(3)
tree.left = TreeNode(5)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left =TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right = TreeNode(1)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)
p = tree.left
q = tree.right

print(Solution().lowestCommonAncestor(tree, p, q))
