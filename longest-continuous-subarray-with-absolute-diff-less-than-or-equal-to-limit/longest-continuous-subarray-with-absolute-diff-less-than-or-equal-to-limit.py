class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxlen = 0
        i = 0
        minqueue = collections.deque([])
        maxqueue = collections.deque([])
        
        for j in range(len(nums)):
            while minqueue and minqueue[-1] > nums[j]:
                minqueue.pop()
            minqueue.append(nums[j])
            while maxqueue and maxqueue[-1] < nums[j]:
                maxqueue.pop()
            maxqueue.append(nums[j])
            
            if maxqueue[0] - minqueue[0] <= limit:
                maxlen = max(maxlen, j-i+1)
                
            else:
                if maxqueue[0] == nums[i]:
                    maxqueue.popleft()
                if minqueue[0] == nums[i]:
                    minqueue.popleft()
                    
                i+=1
                
                
        return maxlen