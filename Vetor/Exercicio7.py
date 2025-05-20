from random import randint

n = []
mult = []
for i in range(20):
    num = randint(1,50)
    n.append(num)
    print(num)
    if num % 5 == 0:
        mult = sum(n) / len(n)
print("Os multiplos de 5 são {}".format(mult))