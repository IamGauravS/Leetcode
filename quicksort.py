
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[start]

    while start < end:

        while start < len(elements) and elements[start] <= pivot:
            start = start+1
        
        while elements[end] > pivot:
            end -= 1

        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]
    return end

def quicksort(elements,start, end):
    if start < end:
        pivot = partition(elements, start,end)

        quicksort(elements, start, pivot-1)
        quicksort(elements, pivot+1, end)


arr = [1,2,11,3,9,3,7,17,0,12,-1]
quicksort(arr, 0, (len(arr)-1))
print(arr)
    
    
