# EXERCIOCIO 04
dias = int(input("Digite a quantidade de dias: " ))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total = segundos + minutos * 60 + horas * 60 * 60 + dias * 60 * 60 * 24
print("O total em segundos é: ", total)
