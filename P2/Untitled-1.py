tmatriz = int(input("Digite o tamanho da matriz: "))
if tmatriz != 0 and tmatriz < 0:
	print("Tamanho inválido!")
else:
	matriz = [0]*tmatriz
	for i in range(tmatriz):
		matriz[i] = [0]*tmatriz
		for j in range(tmatriz):
			matriz[i][j] = i+j
	aux = tmatriz-1
	total = 0
	for i in range(tmatriz):
		total = total + matriz[i][aux]
		aux = aux - 1
	for i in range(tmatriz):
		print(matriz[i])
	print('Média:' , total/float(tmatriz))
print('Fim programa')