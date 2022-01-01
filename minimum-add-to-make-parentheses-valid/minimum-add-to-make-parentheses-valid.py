class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(c)
                
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
                    
        return len(stack)
            