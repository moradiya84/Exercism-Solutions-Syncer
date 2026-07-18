l = []
import random
class Robot:
    def reset(self):
        while True:
            ans = ""
            self.name=""
            num = random.randint(0,25)
            ans += chr(num+ord('A'))
            num = random.randint(0,25)
            ans += chr(num+ord('A'))
            num = random.randint(0,9)
            ans += str(num)
            num = random.randint(0,9)
            ans += str(num)
            num = random.randint(0,9)
            ans += str(num)
            if ans in l:
                continue
            self.name = ans
            l.append(ans)
            break
        
    def __init__(self):
        self.reset()
