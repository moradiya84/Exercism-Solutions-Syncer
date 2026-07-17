def abbreviate(words):
    ans = ""
    k=1
    for c in words:
        if 'a'<=c<='z' or 'A'<=c<='Z':
            if k == 1:
                ans+=c.upper()
                k=0
        elif c == '\'':
            continue
        else:
            k=1
    return ans
            
