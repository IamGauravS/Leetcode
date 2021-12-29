import math
input_arr = [2, 30, 29, 28, 22, 30, 11, -1, 40,-10]



class BubbleSort:
    def sort(self, input_arr):
        for i in range(len(input_arr)-1):
            for j in range(len(input_arr)-1-i):
                if input_arr[j] > input_arr[j+1]:
                    temp = input_arr[j]
                    input_arr[j] = input_arr[j+1]
                    input_arr[j+1] = temp 


        return input_arr


class SelectionSort:
    def sort(self, input_arr):
        for i in range(len(input_arr)-1):
            min_index = i
            for j in range(i+1, len(input_arr)):
                if input_arr[j] < input_arr[min_index]:
                    min_index = j 
            temp = input_arr[i]
            input_arr[i] = input_arr[min_index]
            input_arr[min_index] = temp 


        return input_arr

class InsertionSort:
    def sort(self, input_arr):
        for i in range(len(input_arr)):
            prev = i-1
            current = input_arr[i]
            while prev >= 0 and input_arr[prev] > current:
                input_arr[prev+1] = input_arr[prev]
                prev = prev -1 

            input_arr[prev+1] = current

        return input_arr


sort = BubbleSort()

output= sort.sort(input_arr)
print(output)


sort = SelectionSort()
output = sort.sort(input_arr)
print(output)

sort = InsertionSort()
output = sort.sort(input_arr)
print(output)