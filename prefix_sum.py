import math
input_arr = [1,-3,-3,-5,-6,7,8]



class Prefixsum:

    def prefixSum(self, input_arr):
        max_sum = -math.inf 

        sum_arr = []
        sum_arr.append(input_arr[0])
        for i in range(1, len(input_arr)):
            sum_arr.append(sum_arr[i-1] + input_arr[i])

        for i in range(len(input_arr)):
            for j in range(i, len(input_arr)):

                if i > 0:
                    prefix_sum = sum_arr[j] - sum_arr[i-1]

                if i == 0:
                    prefix_sum = sum_arr[j] 

                
            max_sum = max(prefix_sum, max_sum)

        return max_sum


findmaxsum = Prefixsum()
output = findmaxsum.prefixSum(input_arr)
print(output)




        
