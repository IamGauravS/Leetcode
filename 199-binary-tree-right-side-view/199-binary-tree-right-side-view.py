# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            rightSide = None
            qLen = len(q)
            
            for i in range(qLen):  ## we only iterate till current level length
                node = q.popleft()
                if node:               ## we want the right side so we take the last element
                    rightSide = node
                    
                    q.append(node.left)
                    q.append(node.right)
                    
                    
            if rightSide:
                res.append(rightSide.val)
                
                
        return res