import math
def factors(value):
    l = []
    num =value
    for i in range (2,math.isqrt(num)+1):
        while value%i == 0:
            l.append(i)
            value//=i
    if value!=1:
        l.append(value)
    return l