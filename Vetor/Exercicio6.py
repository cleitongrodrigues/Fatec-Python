from random import randint

l = []
par = []
for i in range(20):
    num = randint(1,50)
    par.append(num)
    print(num)
    if num % 2 == 0:
        media = sum(par) / len(par)
print("A média dos pares é {}".format(media))