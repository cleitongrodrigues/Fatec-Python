usu = []
while len(usu) < 20:
    num = int(input("Digite um número: "))
    usu.append(num)

for i in range(10):
    usu[i], usu[10+1] = usu[10+1], usu[i]

print("Novo array:", usu)