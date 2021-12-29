
def fact(n):
    if n==0:
        return 1 
    ans = n*fact(n-1)

    return ans

#0,1,1,2,3,5,8,13,
# print(fact(3))

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    sum = fibo(n-1) + fibo(n-2)

    return sum 

def firstocc(array, target):
    if array[0] == target:
        return 0
    if len(array) == 1:
        return -1

    value = firstocc(array[1:], target)
    if value >= 0:
        index = 1 + value
    else:
        index = value

    return index

## here instead of checking the zeroeth element we check for the number in
## the remaining subarray if the number is there in the remaining subarray
## we return that number otherwise we check for the number in the zeroth index
## and if it's there we return that one

def lastocc(array, target):
    if len(array) == 0:
        return -1

    subindex = lastocc(array[1:], target)

    if subindex < 0:
        if array[0] == target:
            return 0
        else:
            return -1 

    else:
        return 1+ subindex


print(firstocc([1,2,3,6,6,7],7))
print(lastocc([1,2,3,6,6,7,6],6))