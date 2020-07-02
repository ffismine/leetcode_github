from typing import List

from tag_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)
A.left.left = TreeNode(4)
A.left.right = TreeNode(5)
A.right.left = TreeNode(6)

print(Solution().inorderTraversal(A))
