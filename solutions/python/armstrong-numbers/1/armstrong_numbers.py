def ff(number,l):
    if(number<10) :
        return number**l
    else:
        return (number%10)**l + ff(number//10,l)

def is_armstrong_number(number):
    s=str(number)
    l=len(s)
    return ff(number,l)==number
