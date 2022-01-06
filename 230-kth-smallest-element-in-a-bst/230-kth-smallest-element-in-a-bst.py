# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root 
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left 
                
            ## when this loop stops executing it means we are at last or lowest element
            ## and we went too far so we will pop it and add its right children here
            
            cur = stack.pop()
            n += 1  ## we just visited another node so we increment it by 1
            
            if n == k:
                return cur.val 
            
            cur = cur.right ## now we process the right subtree