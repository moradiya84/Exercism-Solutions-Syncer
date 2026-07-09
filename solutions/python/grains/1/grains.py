def square(number):
    if(number<=0 or number>64):
        raise ValueError("square must be between 1 and 64")
    if(number == 1) :
        return 1
    return 2*square(number-1)

def tot(num):
    if(num==0):
        return 0
    return square(num)+tot(num-1)
def total():
    return tot(64)
