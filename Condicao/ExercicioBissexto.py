ano = int(input("Informe o ano: \n"))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("Ano bissexto")
else:
    print("Ano não bissexto")