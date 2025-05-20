from random import randint

l = []
opcao = int(input("Selecione uma opcao 1 - Numeros normais | 2 - Numeros na ordem inversa: \n"))
for i in range(10):
    num = randint(1, 50)
    l.append(num)

if opcao == 1:
    print("Lista normal:", l)
elif opcao == 2:
    print("Lista invertida:", l[::-1])