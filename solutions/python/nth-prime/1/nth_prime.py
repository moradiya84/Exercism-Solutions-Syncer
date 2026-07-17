import math
def prime(number):
    if number<1:
        raise ValueError("there is no zeroth prime")
    cnt = 0
    i = 2
    while True:
        p=0
        for j in range(2,math.isqrt(i)+1):
            if(i%j == 0):
                p=1
                break

        if p == 0 :
            cnt+=1
        if cnt == number :
            return i
        i+=1
    pass
