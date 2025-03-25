a = float(input("Digite o primeiro angulo do triângulo: \n"))
b = float(input("Digite o segundo angulo do triângulo: \n"))
c = float(input("Digite o terceiro angulo do triângulo: \n"))

if (a + b + c) == 180:
    if a < 90 and b < 90 and c < 90:
        print("Triângulo acutângulo")	
    elif a == 90 or b == 90 or c == 90:
        print("Triângulo retângulo")
    else:
        print("Triângulo obtusângulo")
else:
        print("Os angulos fornecdos não formam um triângulo")