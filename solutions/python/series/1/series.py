def slices(series, length):
    ans = []
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if len(series) == 0:
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    for i in range(len(series)-length+1):
        ans.append(series[i:i+length])
    return ans
