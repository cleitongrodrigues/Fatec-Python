from random import randint

n = []

while len(n) <10:
    num = randint(1,50)
    
    if num not in n:
        n.append(num)
    
print(n)        