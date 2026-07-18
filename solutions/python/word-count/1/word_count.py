def count_words(s):
    d = dict()
    st = 0
    s = s.replace('\n','') + "@"
    for i in range(st, len(s)):
        while not (('A'<=s[st]<='Z') or ('a'<=s[st]<='z') or ('0'<=s[st]<='9')):
            st+=1
            if st == len(s):
                break
        if st == len(s):
            break
            
        if s[i]=="'" and s[i+1].isalpha():
            continue
        if ('A'<=s[i]<='Z' or 'a'<=s[i]<='z'):
            continue
        if i > st:
            d[s[st:i].lower()]=d.get(s[st:i].lower(),0)+1
            st=i+1
        
    return d
        
