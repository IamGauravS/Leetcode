class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        candidate_queue = collections.deque([i for i in range(1, n+1)])
        
       
        
        while len(candidate_queue) > 1:
            for i in range(k-1):
                candidate_queue.append(candidate_queue.popleft())
                
            print(candidate_queue.popleft())
            
            
        return candidate_queue[0]