def is_paired(input_string):
    l = ['{','}','[',']','(',')']
    d = dict()
    d['(']=')'
    d['[']=']'
    d['{']='}'
    d['}']='x'
    d[')']='x'
    d[']']='x'
    l1 = []
    for c in input_string:
        if c in l:
            if len(l1)!=0 and d[l1[-1]]==c:
                l1.pop()
            else:
                l1.append(c)
    if len(l1)==0:
        return True
    return False
