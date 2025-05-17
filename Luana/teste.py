
# Peça para o usuário digitar um número.

# Use um laço for para exibir a tabuada desse número, de 1 a 10.

n = int(input("Digite um número para ver sua tabuada"))
for i in range(0,11):
    resultado = n * i
    print("{} * {} = {}".format(n,i,resultado))