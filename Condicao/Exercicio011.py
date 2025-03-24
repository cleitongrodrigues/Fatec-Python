a = float(input("Digite o primeiro valor: \n"))
b = float(input("Digite o segundo valor: \n"))
c = float(input("Digite o terceiro valor: \n"))

if (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
    print("Todos os valores são pares")
elif a % 2 == 0:
    print("O primeiro valor é par")
elif b % 2 == 0:
    print("O segundo valor é par")
elif c % 2 == 0:
    print("O terceiro valor é par")
else:
    print("Todos os valores são ímpares")