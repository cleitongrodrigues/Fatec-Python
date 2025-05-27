from random import randint

usu = int(input("Digite um número: \n"))
n = []

for i in range(11):
    n.append(randint(1, 50))

print("Números sorteados:", n)

if usu in n:
    print(f"O número {usu} está na lista!")
else:
    print("O número {} não está na lista.".format(usu))
