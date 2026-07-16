def square_root(number):
    l = 0
    r = number
    while l<=r:
        mid = (l+r)//2
        if mid * mid == number:
            return mid
        if mid * mid > number:
            r=mid-1
        else:
            l=mid+1
            
