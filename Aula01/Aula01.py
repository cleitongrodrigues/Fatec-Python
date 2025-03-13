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
