from random import randint

numeros = []
pares = 0
impares = 0
for i in range(10):
    numeros.append(randint(1, 50))

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números gerados:", numeros)
print("Total de números pares:", pares)
print("Total de números ímpares:", impares)
