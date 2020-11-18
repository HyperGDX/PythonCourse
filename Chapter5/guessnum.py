import random


print("Guess Number Game!")
cnum=random.randint(1,100)
g = -1

while g != cnum:
    g = input()
    g = int(g)
    if g == cnum:
        print("right")
    elif g >= cnum:
        print("too big")
    else:
        print("too small")
