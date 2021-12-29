class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        row = [1]*n  ## row is previous row and new row is current row and we 
        ## do not need the whole board just the previous row and the current row
        
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
                
            row = newRow
            
            
        return row[0]
        