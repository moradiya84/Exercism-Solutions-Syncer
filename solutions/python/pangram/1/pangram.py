def is_pangram(sentence):
    sentence=sentence.lower()
    s = set()
    for c in sentence:
        if c>='a' and c<='z':
            s.add(ord(c))
    return len(s)==26    
