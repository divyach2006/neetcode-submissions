# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are null, so they match
        if not p and not q:
            return True
            
        # Base Case 2: One node is null but the other isn't, so they don't match
        if not p or not q:
            return False
            
        # Base Case 3: Both nodes exist but have different values
        if p.val != q.val:
            return False
            
        # Recursive Step: Check if left subtrees match AND right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
