from tag_tree import TreeNode


def treeA():
    A = TreeNode(1)
    A.left = TreeNode(2)
    A.right = TreeNode(3)
    A.left.left = TreeNode(4)
    A.left.right = TreeNode(5)
    A.right.left = TreeNode(6)

    return A
