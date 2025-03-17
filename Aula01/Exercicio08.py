precolitro = float (input("Digite o valor do preço por litro do combustível! \n"))
qtdEconomida = float (input("Digite quantos quilômetros seu veículo faz por litro \n"))
qtdPercorrida = float (input("Digite a distância percorrida! \n"))
consumo = float (qtdPercorrida / qtdEconomida)
valor = float (consumo * precolitro)

print("A quantidade de litros gastos foi de ", consumo, "e o valor em dinheiro foi", valor)
