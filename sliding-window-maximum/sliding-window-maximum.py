class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        q = collections.deque() ## this will contain indecies
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: ## making sure no smaller values are there
                q.pop()
            q.append(r) ## add the new value
            
            
            if l > q[0]:  ## remove the left val if it is outbound we only want to look at the sliding window
                q.popleft()
                
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r += 1
        return output
        
        