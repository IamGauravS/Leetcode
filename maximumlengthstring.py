class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def checkduplicate(s):
            return len(s) != len(set(s))
        
        
        ans = 0
        n = len(arr)
        def backtrack(s, i):
            if i >= n:
                self.ans = max(self.ans, len(s))
                return

            backtrack(s, i+1)
            ns = s + arr[i]
            if checkduplicate(ns):
                backtrack(ns, i+1)

                    
                    
        backtrack("", 0)
        return ans