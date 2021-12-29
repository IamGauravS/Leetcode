import math
input_arr = [10, 22, 28, 29, 30, 40]

target = 54

class SortedPairsum:
    def findmaxsum(self, input_arr, target):
        l = 0
        r = len(input_arr)-1 
        diff = math.inf
        lower=  0
        upper = 0
        while l < r:
            sum = input_arr[l] + input_arr[r]
            if abs(target - sum) < diff:
                diff = abs(target-sum)
                lower = input_arr[l]
                upper = input_arr[r]
            if sum > target:
                r -= 1
            else:
                l += 1 


        return [lower, upper]


findpair = SortedPairsum()
output = findpair.findmaxsum(input_arr, target)
print(output)
