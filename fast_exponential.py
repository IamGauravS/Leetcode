
a= 2
n = 5

def fastexpo(a,n):
    ans = 1 
    while(n>0):
        print(n)
        lastbit = n&1
        if lastbit:
            ans = (ans*a)%p

        a=(a*a)%p 
        n = n>>1

    return ans 

def converttobinary(num):
    answer = 0
    power = 1
    while(num>0):
        lastbit = num&1
        print(lastbit)
        answer = answer+lastbit*power 
        
        power = power*10
        num = num>>1

    return answer

print(converttobinary(4))


