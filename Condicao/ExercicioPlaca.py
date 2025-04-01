placa = int(input("Digite o ultimo numero da placa: \n"))
if (placa == 9) or (placa==0):
    print("Sexta-Feira")
elif placa <=2:
    print("Segunda-Feira")
elif placa<=4:
    print("Terça-Feira")
elif placa<=6:
    print("Quarta-Feira")
elif placa<=8:
    print("Quinta-Feira")
else:
    print("Aos finais de semana todos podem rodar!")
    