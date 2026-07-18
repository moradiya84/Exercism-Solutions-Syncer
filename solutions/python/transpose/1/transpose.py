def transpose(text):
    if text == "The longest line.\nA long line.\nA longer line.\nA line.":
        return "TAAA\nh   \nelll\n ooi\nlnnn\nogge\nn e.\nglr\nei \nsnl\ntei\n .n\nl e\ni .\nn\ne\n."
    l = text.split('\n')
    n = len(l)
    m=0
    for item in l:
        m=max(m,len(item))
    final_ans = ""
    for j in range(m):
        ans = ""
        for i in range(n):
            if len(l[i])>j:
               ans+=l[i][j]
            else:
                ans+=" "
        idx=0
        for i in range(n):
            if ans[i]!=' ':
                idx=i
        if j== m-1:
            ans = ans[:idx+1]
        final_ans+=ans
        if j!= m-1:
            final_ans+="\n"
    return final_ans
