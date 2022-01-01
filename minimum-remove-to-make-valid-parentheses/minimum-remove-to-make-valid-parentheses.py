class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        N = len(s)
        s = list(s)
        
        for i in range(N):
            if s[i] == "(":
                stack.append(i)
                
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""  ## reintilize that character to blank string
                
            
            
        ## stack containing index number of open (
        
        for j in stack:
            s[j] = ""
            
        return "".join(s)
            
            
            
        