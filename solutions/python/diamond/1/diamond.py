def rows(letter):
    m = 2*(ord(letter)-ord('A'))+1
    l = []
    left = m//2
    right = left
    cur = 0
    change = -1
    cur_char='A'
    while cur<m:
        ans = ""
        for i in range(m):
            if i ==left or i == right:
                ans+=cur_char
            else :
                ans+=' '
        l.append(ans)
        left+=change
        right-=change
        if left == -1:
            left = 1
            right = m-2
            change = 1
        cur_char = chr(ord(cur_char)-change)
        cur+=1
    return l
    
