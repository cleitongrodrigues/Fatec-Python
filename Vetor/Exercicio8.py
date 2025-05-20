from random import randint

l = []
multiplos = []
numero = int(input("Digite um núemro para saber seus multiplos: \n"))
for i in range(20):
    num = randint(1,50)
    l.append(num)
    print(num)
    
    if num % numero == 0:
        multiplos.append(num)
print("Os multiplos de {} é {}".format(numero,multiplos))       