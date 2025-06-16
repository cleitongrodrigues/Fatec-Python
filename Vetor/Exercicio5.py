from random import randint
  
numeros = [0] * 6

for i in range(6):
    numeros[i] = [0] * 6
    for j in range(6):
        numeros[i][j] = randint(1,50)
        if numeros[i][j] % 2 != 0:
            print(numeros[i][j])        