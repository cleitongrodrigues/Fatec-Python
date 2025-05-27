from random import randint

A, B, C = [], [], []

for i in range(20):
    n = randint(1, 50)
    A.append(n)

    if n % 2 == 0:
        B.append(n)
    else:
        C.append(n)

print("Vetor completo (A): \n", A)
print("Números pares (B): \n", B)
print("Números ímpares (C): \n", C)