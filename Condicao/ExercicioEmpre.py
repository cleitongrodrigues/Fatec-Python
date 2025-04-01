salario = float(input("Informe o total do saláio: \n"))
prestacao = float(input("Digite o valor da prestação: \n"))
if  prestacao > salario*0.2:
    print("Crédito não concedido")
else:
    print("Crédito concedido!")