def decode(string):
    i=0
    ans = ""
    while i < len(string):
        if '0'<=string[i]<='9':
            if '0'<=string[i+1]<='9':
                num = int(string[i:i+2])
                i+=2
            else:
                num = int(string[i:i+1])
                i+=1
            while num!=0:
                ans += string[i]
                num-=1
        else:
            ans+=string[i]
        i+=1
    return ans
                


def encode(string):
    if(string == ""):
        return string
    cnt=1
    ans = ""
    for i in range(1,len(string)):
        if string[i]!=string[i-1]:
            if cnt!=1:
                ans+=str(cnt)
            ans+=string[i-1]
            cnt=0
        cnt+=1
        
    if cnt != 1:
        ans+=str(cnt)
    ans+=string[-1]
        
    return ans
