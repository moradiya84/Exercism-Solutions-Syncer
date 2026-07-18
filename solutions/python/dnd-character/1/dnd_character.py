import random
def ff():
    l = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    l.sort()
    return l[1]+l[2]+l[3]
class Character:
    def __init__(self):
        self.strength=ff()
        self.dexterity=ff()
        self.constitution=ff()
        self.intelligence=ff()
        self.wisdom=ff()
        self.charisma=ff()
        self.hitpoints=10+modifier(self.constitution)
    def ability(self):
        return ff()
def modifier(value):
    return (value-10)//2
