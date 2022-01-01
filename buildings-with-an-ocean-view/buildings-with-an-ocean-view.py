class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(heights)-1, -1, -1):
            stack.append(i)
            if len(stack) > 1 and heights[stack[-1]] <= heights[stack[-2]]:
                stack.pop()
                
                
                
        return stack[::-1]
                
            