# # # # for item in [3, 4, 5,6 ,7]:
# # # #     print(item)
    
# # # # lista = "olá mundo"
# # # # for item in lista:
# # # #     print(item)
    
# # # # for item in range(5):
# # # #     print("olá mundo")

# # # # for item in range(0,5,1):
# # # #     print("Neymar")
    
    
# # # # numero = int(input("Digite um numero para ver sua tabuada até o 10: \n"))
# # # # for i in range(11):  
# # # #     resultado = i * numero
# # # #     print(f"{i} x {numero} = {resultado}")

# # # # numero = 1    
# # # # while numero < 101:
# # # #     print(numero)
# # # #     numero += 1
 
# # # # numero = 1
# # # # for i in range(100):
# # # #     print(numero)
# # # #     numero += 1

# # # # nome = str(input("Digite um nome: \n"))
# # # # vezes = int(input("Quantas vezes deseja que ele se repita? \n"))
# # # # for i in range(vezes):
# # # #     print(nome)

# # # # numero = 0
# # # # for i in range(100):
# # # #     print(numero + numero)
# # # #     numero += 1
    
# # # # soma = 0
# # # # for numero in range(1, 101):
# # # #     soma += numero
# # # # print(f"A soma de todos os números de 1 a 100 é: {soma}")

# # # # par   = 0
# # # # impar = 0
# # # # for i in range(1,101,1):
# # # #     if (i%2 == 0):
# # # #         par += i
# # # #     else:
# # # #         impar += i
# # # # print("Soma dos numeros pares é: " , par)
# # # # print("Soma dos numeros impares é: " , impar)

# # # # inicio  = int(input("Digite o valor de inicio da lista: \n"))
# # # # fim     = int(input("Digite o valor do fim da lista: \n"))
# # # # divisor = int(input("Digite por qual numero deseja realizar a divisão: \n"))
# # # # if inicio <= fim:
# # # #     for i in range(inicio,fim+1,1):
# # # #         if(i % divisor == 0):
# # # #             print(divisor)
# # # # else:
# # # #     print("Erro")

# # # # n = 1
# # # # while n <= 100:
# # # #     print(n)
# # # #     n += 1
# # # # print()
# # # # for n in range(100,0,-1):
# # # #     print(n)

# # # # import random
# # # # while True:
# # # #     n1 = random.randint(0,10)
# # # #     n2 = random.randint(0,10)
# # # #     mult = n1*n2
# # # #     resposta = int(input(f"Quanto é {n1} X {n2}?\n"))
# # # #     if (resposta == mult):
# # # #         print("Parabéns, você acertou! \n")    
# # # #         r = int(input("Deseja continuar? \n 1 - Sim \n 2 - Não \n"))
# # # #         if (r != 1):
# # # #             break
# # # #     else:
# # # #         print("Que pena, você errou! \n")
# # # #         r = int(input("Deseja tentar novamente? \n 1 - Sim \n 2 - Não \n"))
# # # #         if (r != 1):
# # # #             break

# # # import random
# # # while True:
# # #     operacao = input("Qual tipo de operação deseja resolver? \n * - Multiplicação \n / - divisão \n + - Adição \n - - Subtração \n")
# # #     if(operacao == '*'):    
# # #         n1 = random.randint(0,10)
# # #         n2 = random.randint(0,10)
# # #         resultado = n1 * n2
# # #         resposta = int(input(f"Quanto é {n1} x {n2}?\n"))
# # #         if (resposta == resultado):
# # #             print("Parabéns, você acertou! \n")    
# # #             r = int(input("Deseja continuar? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #         else:
# # #             print("Que pena, você errou! \n")
# # #             r = int(input("Deseja tentar novamente? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #     elif(operacao == '/'):        
# # #         n1 = random.randint(0,10)
# # #         n2 = random.randint(1,10)
# # #         resultado = n1 / n2
# # #         resposta = float(input(f"Quanto é {n1} / {n2}?\n"))
# # #         if (resposta == resultado):
# # #             print("Parabéns, você acertou! \n")    
# # #             r = int(input("Deseja continuar? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #         else:
# # #             print("Que pena, você errou! \n")
# # #             r = int(input("Deseja tentar novamente? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #     elif(operacao == '+'):
# # #         n1 = random.randint(0,10)
# # #         n2 = random.randint(0,10)
# # #         resultado = n1 + n2
# # #         resposta = int(input(f"Quanto é {n1} + {n2}?\n"))
# # #         if (resposta == resultado):
# # #             print("Parabéns, você acertou! \n")    
# # #             r = int(input("Deseja continuar? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #         else:
# # #             print("Que pena, você errou! \n")
# # #             r = int(input("Deseja tentar novamente? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #     elif(operacao == '-'):
# # #         n1 = random.randint(0,10)
# # #         n2 = random.randint(0,10)
# # #         resultado = n1 - n2
# # #         resposta = int(input(f"Quanto é {n1} - {n2}?\n"))
# # #         if (resposta == resultado):
# # #             print("Parabéns, você acertou! \n")    
# # #             r = int(input("Deseja continuar? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #         else:
# # #             print("Que pena, você errou! \n")
# # #             r = int(input("Deseja tentar novamente? \n 1 - Sim \n 2 - Não \n"))
# # #             if (r != 1):
# # #                 break
# # #     else:
# # #         print("Operação inválida!")
# # #         break

# # pares   = 0
# # impares = 0
# # print("Digite 10 números para descobrir a soma dos pares e ímpares: \n")
# # for i in range(10):
# #     n = int(input())
# #     if n % 2 == 0:
# #         pares += n
# #     else:
# #         impares += n
# # print(f"A soma dos números pares é: {pares} e a soma dos ímpares é: {impares}")

# qtd = int(input("Quantas médias você deseja calcular? \n"))

# for i in range(qtd):
#     n1 = float(input("Digite a primeira nota: \n"))
#     n2 = float(input("Digite a segunda nota: \n"))
#     media = (n1 + n2) / 2
#     print(f"A média das notas {n1} e {n2} é: {media}")

# import random

# maior = 0
# for i in range(20):
#     n1 = random.randint(0,100)   
#     print(n1)
#     if n1 > maior:
#         maior = n1
# print("O maior número gerado é",maior)

# for n in range(1000,198,-3):
#     print(n, end=' ')

# num = 0
# inicio = 1
# n = int(input("Digite quantos números da sequência de Fibonacci você quer ver: "))

# for i in range(n):
#     print(num)
#     p = inicio + num 
#     num = inicio
#     inicio = p       
    
# n = int(input("Digite quantos números da sequência de Fibonacci você quer ver: "))
# if n <= 0:
#     print("Por favor, digite um número maior que zero.")
# else:
#     a = 0
#     b = 1
#     print("Sequência de Fibonacci:")
#     for i in range(n):
#         print(a)         
#         proximo = a + b  
#         a = b            
#         b = proximo

while True:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if num1 < num2:
            soma = 0  
            for i in range(num1, num2 + 1):  
                soma += i  
            print(f"A soma dos números inteiros entre {num1} e {num2} é: {soma}")
        else:
            print("O primeiro número deve ser menor que o segundo. Tente novamente.")

        repetir = int(input("Deseja tentar novamente? 1 - Sim 0 - Não: "))
        if repetir == 0:
            break  