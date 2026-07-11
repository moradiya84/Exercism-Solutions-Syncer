def is_isogram(phrase):
    my_set = set()
    fre = [0]*26
    for c in phrase:
        if(c>='a' and c<='z') or (c>='A' and c<='Z'):
            fre[ord(c.lower())-ord('a')]+=1
    for num in fre:
        if num>1:
            return False
    return True
