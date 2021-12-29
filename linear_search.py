import math

## return index of a given element in the array

input_arr = [1,3,4,5,5,6,7,8]

class Liner_search:
    def linear_search(self, nums, target):
        output_list = []
        for i in range(len(nums)):
            if nums[i] == target:
                output_list.append(i)

        return output_list



searcher = Liner_search()

output = searcher.linear_search(input_arr, 5)

print(output)
