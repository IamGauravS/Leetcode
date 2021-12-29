import numpy as np
input = 13
## binary representaion of 13 is 1101 so second bit from right is 9
# if (input&1):
#     print("odd")
# else:
#     print("even")

# print(input&1)
## to get the ith bit of a number we need to left shift
## 1 by i th times so that it comes just below the i th bit
## and then do an and with 1 then again do a right shift
## we cant use "and" here because we dont want output from other 1's in the binary input
def getithbit(n: int, i: int ):
    print("binary n is: "+  str(np.binary_repr(n, width=8)))
    mask = (1<<(i-1))
    print("binary mask is: " +  str(np.binary_repr(mask, width=8)))
    output = (n&mask) >> (i-1) 
    print("binary output is: " + str( np.binary_repr(output, width=8)))
    print(output)



## clear the ith bit. You need to create a number in which ith bit is zero
# and rest everything is same we can create a mask using left shift i and then
# take a not of that mask and then take an and of that number

def clearithbit(n: int, i: int ):
    print("binary n is: "+  str(np.binary_repr(n, width=8)))
    mask = ~(1<<(i-1))
    print("binary mask is: " +  str(np.binary_repr(mask, width=8)))
    output = (n&mask)
    print("binary output is: " + str( np.binary_repr(output, width=8)))
    print(output)
    return output

## set i th bit basically means changing ith bit to one to do that we can take a mask
## with all zeros and 1 at i th position and then take an and 

def setithbit(n:int, i:int):
    print("binary n is: " + str(np.binary_repr(n,width=8)))
    mask = (1<<i)
    print("Binary mask is: " + str(np.binary_repr(mask, 8)))
    output = (n|mask)
    print("binary output is: " + str(np.binary_repr(output,8)))

## set ith bit to v, v can be anything either 0 or1 to achieve this we first clear the ith
## bit and then take a mask of V and do an or operation
def updateithbit(n:int, i:int, v:int):
    print("binary n2 is: " + str(np.binary_repr(n,width=8)))
    output = clearithbit(n,i)
    mask = (v<<(i-1))
    print("Binary mask2 is: " + str(np.binary_repr(mask, 8)))
    print("binary output2 is: " + str(np.binary_repr(output,8)))
    output = (output|mask)
    print("binary output3 is: " + str(np.binary_repr(output,8)))


## for clearing last i bits we need something like 11110000 where last i items are zero
## and then we can do an and with the original binary representation. For getting 11110000
## we need to do a left shift of 11111111 by i places. 11111111 is basically -1 
def clearibit(n:int, i:int):
    print("binary n is: " + str(np.binary_repr(n,width=8)))
    mask = (-1<<i)
    print("Binary mask is: " + str(np.binary_repr(mask, 8)))
    output = (n&mask)
    print("binary output is: " + str(np.binary_repr(output,8)))


# binary n is: 00001101
# Binary mask1 is: 11100000
# Binary mask2 is: 00000011
# Binary mask is: 11100011
# Binary output is: 00000001
def clearbitrange(n:int, i:int, j:int):
    print("binary n is: " + str(np.binary_repr(n,width=8)))
    mask1 = (~0)<<(j+1)
    print("Binary mask1 is: " + str(np.binary_repr(mask1, 8)))
    mask2 = (1<<(i))-1
    print("Binary mask2 is: " + str(np.binary_repr(mask2, 8)))
    mask = mask1|mask2 
    print("Binary mask is: " + str(np.binary_repr(mask, 8)))
    output = n&mask 
    print("Binary output is: " + str(np.binary_repr(output, 8)))


def countbit(n: int):
    count = 0
    while(n>0):
        count = count+(n&1)
        n = n>>1

    return count
# print(np.binary_repr(-8, width=8))
clearbitrange(input,2,4)

