# faca um programa que leia dois vetores (AeB) de 10 elementos inteiros
# e calcule um terceiro vetor(C) formado somente por elementos que existem
# em ambos os vetores A e B, não importando suas posicoes (intersecção)

A, B, C = [],[],[]

print("Digite 10 números para a array A:")
for i in range(10):
    num = int(input())
    A.append(num)

print("Digite 10 números para a array B:")
for i in range(10):
    num = int(input())
    B.append(num)

for num in A:
    if num in B and num not in C: 
        C.append(num)

print("Array C: \n", C)
