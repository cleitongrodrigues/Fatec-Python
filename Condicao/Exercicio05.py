cpElevador = float(input("Digite a capacidade máxima de peso suportada: \n"))
p1 = float(input("Digite o peso da primeira pessoa: \n"))
p2 = float(input("Digite o peso da segunda pessoa: \n"))
p3 = float(input("Digite o peso da terceira pessoa: \n"))
p4 = float(input("Digite o peso da quarta pessoa: \n"))
p5 = float(input("Digite o peso da ultima pessoa: \n"))
ttPeso = (p1 + p2 + p3 + p4 + p5)

if (ttPeso > cpElevador):
    print("Capacidade excedida!")
elif (ttPeso < cpElevador):
    print("Pode subir")
else:
    print("Capacidade máxima atingida")