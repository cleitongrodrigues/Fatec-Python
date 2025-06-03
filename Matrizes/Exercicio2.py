# M = [1,2,3],[4,5,6]
# print(M)

# M = [0] * 2
# for i in range(2):
#     M[i] = [0] * 3
#     for j in range(3):
#         M[i] [j] = 1
# print(M)
# M = [0] * 2
# M[0] = [1,1,1]
# M[1] = [2,2,2]
# print(M)

# M = [[1,2,3],[4,5,6]]
# for i in range(0,2):
#     for j in range(0,3):
#         print("[{:^3}] ".format(M[i][j], end=''))
#     print()

# M = [0] * 2
# for i in range(0,2):
#     M[i] = [0] * 3
#     for j in range(0,3):
#         M[i][j] = int(input("Digite o valor [{}][{}] -> ".format(i,j)))
#     print(M)
    
# M = []
# for i in range(0,2):
#     M.append([])
#     for j in range(0,3):
#         M[i].append(int(input("Digite o valor [{}][{}] -> ".format(i,j))))
# print(M)

# from random import randint
# M = []
# for i in range(0,2):
#     M.append([])
#     for j in range(0,3):
#         M[i].append(randint(1,50))
# print(M)

# M = [0] * 2
# for i in range(0,2):
#     M[i] = [0] * 3
#     for j in range(0,3):
#         M[i][j] = int(input("Digite os valores da matriz [{}][{}]".format(i,j)))
# print(M)
# soma = sum(map(sum, M))
# print("Soma de todos os elementos: ", soma)

# from random import randint 

# M = [0]*10
# for i in range(10):
#     M[i] = [0] * 10
#     for j in range(10):
#         M[i][j] = randint(1,50)

# total = sum(map(sum, M))        
# media = total / len(M)
# print(M)
# print("A média é: ", media)        

# --------------------------------------------------------------------------
#  faça um programa em python que gere uma matriz 10 x 10
#  de inteiros aleatorios entre 5 e 38, imprima a matriz e 
#  a soma de todos os elementos de cada linha
# from random import randint

# M = [0] * 10
# for i in range(10):
#     M[i] = [0] * 10
#     for j in range(10):
#         M[i][j] = randint(5, 38)

# # Exibindo cada linha da matriz
# for i in range(10):
#     print(f"Linha {i + 1}: {M[i]}")

# # Exibindo a soma de cada linha
# for i in range(10):
#     soma = sum(M[i])
#     print(f"Soma da linha {i + 1}: {soma}")
# ---------------------------------------------------------------------------

from random import randint

M = [0] * 10
for i in range(10):
    M[i] = [0] * 10
    for j in range(10):
        M[i][j] = randint(1, 50)

for c in M:
    print(c)

for j in range(10):
    menor = M[0][j]  
    for i in range(10):
        if M[i][j] < menor:
            menor = M[i][j]
    print("O menor elemento da coluna", j + 1, "é:", menor)
