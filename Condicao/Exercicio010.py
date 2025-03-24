a = float(input("Digite o primeiro lado do triângulo: \n"))
b = float(input("Digite o segundo lado do triângulo: \n"))
c = float(input("Digite o terceiro lado do triângulo: \n"))

if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b and b == c:
        print("Triângulo equilátero")
    elif a == b or b == c or a == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os lados fornecidos não formam um triângulo")