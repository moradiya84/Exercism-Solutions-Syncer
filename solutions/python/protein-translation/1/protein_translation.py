def proteins(strand):
    d = {
        "AUG": "Methionine",
    
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
    
        "UUA": "Leucine",
        "UUG": "Leucine",
    
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
    
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
    
        "UGU": "Cysteine",
        "UGC": "Cysteine",
    
        "UGG": "Tryptophan",
    
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
    l = []
    for i in range(0,len(strand),3):
        if d[strand[i:i+3]]=='STOP':
            break
        l.append(d[strand[i:i+3]])
    return l
        
