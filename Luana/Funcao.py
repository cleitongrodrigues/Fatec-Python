n = int(input())
p = []
soma = 0

for i in range(n):
    p.append(int(input()))
    
for j in p:
    if j == 1:
        soma += 2
    else:
        soma += 1
        
print('par' if soma % 2 == 0 else 'impar')        
        

# CASO PEÇA PARA DIGITAR AS ENTRADAS EM UMA LINHA

p = list(map(int, input().split()))
soma = 0
for j in p:
    if j == 1:
        soma += 2
    else:
        soma += 1

print('par' if soma % 2 == 0 else 'impar')

