import math
input_arr = [1,-3,-3,-5,-6,7,8]



class kadanesum:
    def findmaxsum(self, input_arr):
        maxsum = -math.inf
        curr_sum = 0
        for num in input_arr:
            curr_sum = curr_sum + num 
            if curr_sum < 0:
                curr_sum = 0
            maxsum = max(curr_sum, maxsum)


        return maxsum



findsum = kadanesum()

output = findsum.findmaxsum(input_arr)
print(output)
