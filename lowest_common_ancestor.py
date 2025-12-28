"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as 
the lowest node in T that has both p and q as 
descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(self, root, p, q):

    parent_val = root.val

    p_val = p.val
    q_val = q.val

    if p_val > parent_val and q_val > parent_val:
        return self.lowestCommonAncestor(root.right, p, q)
    elif p_val < parent_val and q_val < parent_val:
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        return root
