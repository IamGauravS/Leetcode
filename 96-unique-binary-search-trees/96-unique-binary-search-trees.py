class Solution:
    def numTrees(self, n: int) -> int:
        ## numTree[4] = numTree[0] * numTree[3] + numTree[1]*numTree[3] + numTree[2]*numTree[2]
        
        numTree = [1] * (n+1)
        
        if n == 0 or n == 1:
            return 1
        
        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                leftsubtree = root - 1
                rightsubtree = nodes - root
                total += numTree[leftsubtree] * numTree[rightsubtree]
                
            numTree[nodes] = total
            
            
        return numTree[n]