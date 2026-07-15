def distance(a, b):
    if len(a) != len(b):
        raise ValueError("Strands must be of equal length.")
    ans=0
    for i in range(len(a)):
        ans += (a[i]!=b[i])
    return ans
