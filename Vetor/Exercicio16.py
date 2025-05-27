A, B, C = [], [], []

print("Digite 10 números para a lista A:")
for i in range(10):
    num = int(input(f"Número {i+1}: "))
    A.append(num)

print("Digite 10 números para a lista B:")
for i in range(10):
    num = int(input(f"Número {i+1}: "))
    B.append(num)

for num in A:
    if num not in C:
        C.append(num)

for num in B:
    if num not in C:
        C.append(num)

print("\nLista C (união sem repetição):")
print(C)