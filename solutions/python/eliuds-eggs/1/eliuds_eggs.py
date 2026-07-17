def egg_count(display_value):
    cur = 1
    ans = 0
    while display_value!=0:
        ans+=(display_value%2)
        display_value//=2
    return ans
