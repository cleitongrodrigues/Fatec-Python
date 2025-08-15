n = int(input())
soma = 0

for i in range(n):
    p = int(input())  # posição do primo
    cont = 0
    num = 1
    
    # acha o primo que está na posição p
    while cont < p:
        num += 1
        eh_primo = True
        for j in range(2, num):
            if num % j == 0:
                eh_primo = False
                break
        if eh_primo:
            cont += 1
    
    soma += num  # soma o primo encontrado

if soma % 2 == 0:
    print('par')
else:
    print('impar')
