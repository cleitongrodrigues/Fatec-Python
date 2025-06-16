# from random import randint

# a = [] * 12
# soma = 0
# nAnt = 0
# for i in range(12):
#     a.append(randint(1,50))
#     nAnt = a[i] 
#     soma = soma + nAnt

# print("Vetor: ",a)
# print("Soma: ",soma) 

from random import randint

M = [0] * 5
for i in range(5):
    M[i] = [0] * 4
    for j in range(4):
        M[i][j] = randint(1,20)
  
for i in range(5):
     print(f"Linha {i + 1}: {M[i]}")

for i in range(5):
    soma = sum(M[i])
    print(f"Soma da linha {i + 1}: {soma}")

