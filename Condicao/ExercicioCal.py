n1 = float(input("Digite o primeiro numero: \n"))
n2 = float(input("Digite o segundo numero: \n"))
operacao = str(input("Digite a operação desejada: \n se + : adição \n - : subtração \n se * : Multiplicação \n e / : divisão \n"))
if operacao == '+':
    r = n1 + n2
    print(r)
elif operacao == '-':
    r = n1 - n2
    print(r)
elif operacao == '*':
    r = n1 * n2
    print(r)
elif operacao == '//':
    r = n1 / n2
    print(r)
else:
    print("Inválido")