def merge(a,b,arr):
    m = len(a)
    n = len(b)
    i = 0
    j=0
    k = 0
    while i< m and j<n:
        if a[i] < b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
        
    while i<m:
        arr[k] = a[i]
        i+=1
        k+=1
    while j<n:
        arr[k] = b[j]
        j+=1 
        k+=1

    return 


def mergesort(arr):
    if len(arr)<=1:
        return 

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]
   
    mergesort(left)
    mergesort(right)
  
    merge(left,right,arr)


arr = [2,3,7,1,-1,11]
print(mergesort(arr))
print(arr)