arr = [0,1,2,0,1,2,0]


start = 0
end = len(arr)-1
m = 0

for i in range(len(arr)):
    if arr[i] == 1:
        arr[i], arr[start] = arr[start], arr[i]
        start = start+1
    elif arr[i] == 2:
        arr[i], arr[end] = arr[end], arr[i]
        end = end-1
    else :
        if arr[i+1] == 1:
            arr[i], arr[i+1] = arr[i+1], arr[i]

        if arr[i-1] == 2:
            arr[i], arr[i-1] = arr[i-1], arr[i]




print(arr)

