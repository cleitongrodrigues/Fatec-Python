ttEleitores = int (input("Digite o numero de eleitores: \n"))
vtBranco = int (input("Digite a quantidade de votos em branco: \n"))
vtNulo = int (input("Digite a quantidade de votos nulos: \n"))
vtValido = int (input("Digite o número de votos validados: \n"))
prcVtBranco = (vtBranco / ttEleitores) * 100, "%"
prcVtNulo = (vtNulo / ttEleitores) * 100, "%"
prcVtvalido = (vtValido / ttEleitores) * 100, "%"

print("A quantidade em percentual de brancos é: ", prcVtBranco, "em nulos é: ",
       prcVtNulo, "e em válidos é: ",prcVtvalido)
print("Total de eleitores foi de: ",ttEleitores)