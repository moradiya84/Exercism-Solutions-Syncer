class Luhn:
    def __init__(self, card_num):
        self.s=card_num

    def valid(self):
        
        ss = str(self.s).replace(' ','')
        for i in ss:
            if '0'<=i<='9':
                continue
            return False
        if len(ss)<2:
            return False
        sum=0
        for i in range(-1,-len(ss)-1,-1):
            if (-i)%2 == 1:
                sum+=int(ss[i])
            else:
                x = int(ss[i])
                x=2*x
                if x>=10:
                    x-=9
                sum+=x

        return sum%10 == 0
            
