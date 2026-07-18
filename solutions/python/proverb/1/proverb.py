def proverb(*l,qualifier = None):
    ans = []
    if len(l)==0:
        return ans
    
    for i in range(1,len(l)):
        ans.append(f"For want of a {l[i-1]} the {l[i]} was lost.")
    if qualifier == None:
        ans.append(f"And all for the want of a {l[0]}.")
    else:
        ans.append(f"And all for the want of a {qualifier} {l[0]}.")
    
    return ans
