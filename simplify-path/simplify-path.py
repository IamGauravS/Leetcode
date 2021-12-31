class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        
        for c in path + "/":   ## we added / to get the last cur inside
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            
            else:
                cur += c 
                
                
        return "/" + "/".join(stack)   ## we want our string to start with /