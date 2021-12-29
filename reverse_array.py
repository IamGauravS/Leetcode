input_arr = [1,3,3,5,6,7,8]

class ReverseArray:

    def reversearray(self, input_arr):

        start = 0
        end = len(input_arr) -1
        mid = (start+end)//2

        while start < end:
            temp = input_arr[start]
            input_arr[start] = input_arr[end]
            input_arr[end] = temp 

            start += 1 
            end -= 1 

        return input_arr


reverse = ReverseArray()

output = reverse.reversearray(input_arr)
print(output)