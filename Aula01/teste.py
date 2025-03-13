#  PRIMEIRO TESTE
idade = 22
print("Lysis tem " , idade , " anos")
print("João tem %d anos" %idade)
print("João tem {} anos" .format(idade))

# SEGUNDO TESTE
nome = "João"
idade = 22
valor = 51.34
print(nome,"de",idade,"anos tem R$",valor)
print("{} de {} anos tem R$ {}".format(nome,idade,valor))
print(f"{nome} de {idade} anos tem R$ {valor}")

# TERCEIRO TESTE
nome = "João"
idade = 22
valor = 51.34
print("%s de %d anos tem R$ %.2f" %(nome,idade,valor))

# QUARTO TESTE
print("informe seu nome: ")
nome = input ()
print("Olá, %s" %nome)

# QUINTO TESTE
nome = input("informe seu nome: ")
print("Olá, %s" %nome)

# SEXTO TESTE
nome = str (input("informe seu nome "))
nasc = int (input("informe ano de nascimento "))
hoje = int (input("informe ano atual "))
idade = hoje - nasc
print("Olá, %s" %nome)
print("você possui em torno de %d anos de idade" %idade)

# EXERCIOCIO 01
A = 10
B = 20
print("valor de A:",A)
print("valor de B:", B)
C = A
A = B
B = C
print("valor de A:",A)
print("valor de B:", B)

# EXERCIOCIO 02 - UTILIZANDO TUPLAS
a = "Valor de A = 10"
b = "Valor de B = 20"
a,b = b,a
print("Valor de A ", A , "Valor de B", B)

# EXERCIOCIO 03
nome = input("informe seu nome: ")
tel = input("informe seu telefone: ")
end = input("informe seu endereço: ")
print("Olá", nome, "seu telefone é", tel, "e você mora na rua", end)    

# EXERCIOCIO 04
dias = int(input("Digite a quantidade de dias: " ))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total = segundos + minutos * 60 + horas * 60 * 60 + dias * 60 * 60 * 24
print("O total em segundos é: ", total)

# EXERCIOCIO 05
salario = int(input("Digite o salário atual: "))
reajuste = int(input("Digite o valor do reajuste: "))
Novo = ((salario*reajuste/100) + salario)
print("Seu salário era de ",salario, "e agora é de :",Novo)