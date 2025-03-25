idade = int(input("Informe a idade do nadador: \n"))
if (idade >= 5) and (idade <= 7):
    print("Categoria Infantil A")
elif (idade >7) and (idade<=11):
    print("Categoria Infantil B")
elif (idade > 11) and (idade <= 13):
    print("Categoria Juvenil A")
elif (idade > 13) and (idade <= 17):
    print("Categoria Juvenil B")
else:
    print("Categoria Adulto")