

input_arr = [1,3,5,7]

target = 3

class BinarySearch:
    def binarysearch(self, input_arr, target):
        start = 0
        end = len(input_arr)

        while(start<=end):
            mid = (start+end)//2

            if input_arr[mid] == target:
                return mid 

            elif input_arr[mid] > target:
                end = mid - 1
            
            else:
                start = mid + 1


        return -1 


search = BinarySearch()

output = search.binarysearch(input_arr, target)
print(output)


