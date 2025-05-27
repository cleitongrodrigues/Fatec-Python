from random import randint

numeros = []

for i in range(10):
    n = randint(1, 50)
    numeros.append(n)

print("Vetor antes da ordenação:")
print(numeros)

tamanho = len(numeros)
for i in range(tamanho):
    for j in range(0, tamanho - i - 1):

        if numeros[j] > numeros[j + 1]:
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp

print("Vetor após a ordenação:")
print(numeros)
