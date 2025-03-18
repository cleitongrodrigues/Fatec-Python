volume = str(input("Digite de qual recepiente você deseja calcular o volume \n"
"L - Lata de óleo \n"
"C - Caixa de papelão \n"))
calulo = float
if volume == "l" or volume == "L":
    altura = float(input("Digite a altura da lata: \n"))
    raio = float(input("Digite o valor do raio \n"))
    calculo = 3.14 * (raio ** 2) * altura
    print("O volume da lata de óleo é: ",calculo)
elif volume == "c" or volume == "C":
    altura = float(input("Digite a altura da caixa \n"))
    comprimento = float(input("Digite o comprimento da caixa \n"))
    largura = float(input("Digite a largura da caixa \n"))
    calculo = altura * largura * comprimento
    print("O volume da caixa é de: ",calculo)

