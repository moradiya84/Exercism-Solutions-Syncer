def rotate(text, key):
    key%=26
    ans=""
    for i in range(len(text)):
        if(text[i]>='a' and text[i]<='z'):
            x=ord(text[i])-ord('a');
            x+=key;
            x%=26;
            x+=ord('a')
            ans+=chr(x)
        elif(text[i]>='A' and text[i]<='Z'):
            x=ord(text[i])-ord('A');
            x+=key;
            x%=26;
            x+=ord('A')
            ans+=chr(x)
        else:
            ans+=text[i]

    return ans
    