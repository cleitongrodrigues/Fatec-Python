a = int(input("Informe um valor: \n"))
faixa1 = range(0,10)
faixa2 = range(10,20)
if a<0:
    print("Número negativo")
elif a in faixa1:
    print("Número positivo menor que 10")
elif a in faixa2:
    print("Número positivo menor que 20")
else:
    print("Número positivo maior ou igual a 20")