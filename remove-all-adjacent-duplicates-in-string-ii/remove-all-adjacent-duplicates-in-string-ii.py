class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    
            else:
                stack.append([c, 1])
                
        result = ''       
        for arr in stack:
            result += (arr[0] * arr[1])  ## character times no of occurance
            
        return result
               