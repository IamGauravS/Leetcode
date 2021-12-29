import collections
class Solution:
     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            counts = collections.defaultdict(int)
            N = len(nums)
            for x in nums:
                counts[x] +=1 
                
            ans = []
            def recurse(N_left, current_array):
                if N_left == 0:
                    ans.append(current_array[:])
                    return 
                
                for x in counts.keys():
                    if counts[x] > 0:
                        counts[x] -=1
                        recurse(N_left-1, current_array+[x])
                        counts[x] +=1
                        
                        
            recurse(N, [])
            return ans
    
        
      