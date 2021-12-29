input_arr = [1,3,3,5,6,7,8]

class getSubarray:
    def getsubarray(self,nums):
        output_array = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                temp_array = []
                for k in range(i,j+1):
                    temp_array.append(nums[k])
                output_array.append(temp_array)



        return output_array


output = getSubarray()

output_array = output.getsubarray(nums = input_arr)
print(len(output_array))
print(output_array)
