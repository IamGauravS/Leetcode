class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        stack.append(-1)
        for i  in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    temp = i - stack[-1]
                    res = max(temp, res)
                    
            
        
        return res