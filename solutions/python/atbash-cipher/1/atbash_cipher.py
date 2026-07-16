plain = "abcdefghijklmnopqrstuvwxyz"

def encode(plain_text):
    plain_text=plain_text.lower()
    ans = ""
    cnt = 0
    for c in plain_text:
        if (c not in plain) and not(ord('1')<=ord(c)<=ord('9')) :
            continue
        cnt+=1
        if c in plain:
            pos = ord(c)-ord('a')
            new_pos = 25-pos
            ans += plain[new_pos]
        else:
            ans+=c
        if cnt==5:
            ans+=' '
            cnt=0
    if len(ans)!=0 and ans[-1]==' ':
        ans = ans[:-1]
    return ans

def decode(ciphered_text):
    ciphered_text=ciphered_text.lower()
    ans = ''
    for c in ciphered_text:
        if c == ' ':
            continue
        if c not in plain:
            ans+=c
            continue
        pos = ord(c)-ord('a')
        new_pos = 25-pos
        ans += plain[new_pos]
    return ans
