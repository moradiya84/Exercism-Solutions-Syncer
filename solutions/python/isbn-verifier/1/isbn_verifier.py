def is_valid(isbn):
    sum=0
    t=10
    for c in isbn:
        if ord(c)>=ord('0') and ord(c)<=ord('9'):
            sum+=(t*(ord(c)-ord('0')))
            t-=1
        elif c!='-':
            if c!='X' or t!=1:
                return False
            
            sum+=(t*10)
            t-=1
    sum%=11
    if t!=0:
        return False
    return sum==0
