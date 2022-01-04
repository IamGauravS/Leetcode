# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def valid(node, left, right):
            if not node:
                return True ## empty binary search tree is still a true tree
            
            
            if not(node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and ## left side
            valid(node.right, node.val, right))  ## right subtree
        
        
        
        return valid(root, float("-inf"), float("+inf"))