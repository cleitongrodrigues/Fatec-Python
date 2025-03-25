a = float(input("Digite o valor de A: \n"))
b = float(input("Digite o valor de B: \n"))
c = float(input("Digite o valor de C: \n"))
d = float(input("Digite o valor de D: \n"))

if (b > c) and (d > a) and ((c + d) > (a + b)) and (c > 0 and d > 0) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores não aceitos")