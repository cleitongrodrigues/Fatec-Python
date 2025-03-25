valor = int(input("Informe seu valor de saque: "
"Lembrando que temos notas de R$10,00 | R$20,00 | R$50,00 e R$100,00\n"))
if valor % 10 == 0:
    valor100 = valor // 100
    sobra100 = valor % 100

    valor50 = sobra100 // 50
    sobra50 = sobra100 % 50

    valor20 = sobra50 // 20
    sobra20 = sobra50 % 20

    valor10 = sobra20 // 10
    print("Notas de R$100,00: ", valor100)
    print("Notas de R$50,00: ", valor50)
    print("Notas de R$20,00: ", valor20)
    print("Notas de R$10,00: ", valor10) 
else:
    print("Valor inválido")
