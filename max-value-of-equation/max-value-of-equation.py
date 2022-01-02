from heapq import *

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        p = [] ## the difference between x and y and position
        ans = float(-inf)
        for i in range(len(points)):
            while p and points[i][0] - p[0][1] > k: ## checking with previous point
                ## and popping them if they are more then k if the diff is more than k
                ## now then it will further increase in future
                heappop(p)
                
            if p:
                ans  = max(ans, points[i][0] + points[i][1] - p[0][0] )
                
            heappush(p, [points[i][0] - points[i][1], points[i][0]]) ## insert x value and difference
            
            
            
        return ans
                
        