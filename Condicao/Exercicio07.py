op = int(input("Selecione a operação como 1 ou 2 \n"))
base = float(input("Digite o valor da base \n"))
altura = float(input("Digite o valor da altura \n"))

if op == 1:
    area = base * altura
    print("A area é: ", area)
elif op == 2:
    area = (base * altura) / 2
    print("A area é: ", area)   