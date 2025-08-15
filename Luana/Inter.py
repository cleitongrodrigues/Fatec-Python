# --- PASSO 1: LER E GUARDAR OS DADOS DOS CLIENTES ---

# Vamos criar uma lista vazia. Cada item que guardaremos nela será
# uma pequena lista ou tupla contendo o par [usuario, senha].
# Ex: [['ana', 'Senha123'], ['bruno', 'OutraSenha']]
lista_de_clientes = []

print("Digite os pares de usuário e senha. Digite ACABOU para finalizar.")

# Loop "infinito" que só vai parar quando encontrarmos 'ACABOU'
while True:
    # O bloco try/except ajuda a evitar erros se a entrada acabar de repente.
    try:
        linha_lida = input()
        
        # Verificamos a condição de parada
        if linha_lida == "ACABOU":
            break
            
        # Se a linha não for a de parada, separamos o usuário da senha.
        # O .split() quebra a string onde houver espaços.
        usuario, senha = linha_lida.split()
        
        # Adicionamos o par [usuario, senha] à nossa lista principal.
        lista_de_clientes.append( [usuario, senha] )

    except EOFError:
        break

print("\n--- PROCESSANDO E IMPRIMINDO OS RESULTADOS ---\n")

# --- PASSO 2: ORDENAR A LISTA ---

# Agora que temos todos os clientes na lista, podemos ordená-la.
# O comando .sort() para uma lista de listas/tuplas ordena
# automaticamente pelo primeiro item de cada par (neste caso, o nome do usuário).
lista_de_clientes.sort()


# --- PASSO 3: PROCESSAR CADA CLIENTE E IMPRIMIR ---

# Agora fazemos um loop pela nossa lista, que já está em ordem alfabética.
for cliente in lista_de_clientes:
    
    # Para cada 'cliente' na lista, pegamos o nome de usuário e a senha.
    usuario_atual = cliente[0]
    senha_atual = cliente[1]
    
    # --- Início do cálculo do Hash para o cliente atual ---
    
    # 3.1: Calcular o número S
    soma_s = 0
    posicao_do_caractere = 1
    for caractere in senha_atual:
        codigo_ascii = ord(caractere)
        soma_s = soma_s + (codigo_ascii * posicao_do_caractere)
        posicao_do_caractere = posicao_do_caractere + 1
    
    # Guardamos o valor original de S antes de modificá-lo
    s_original = soma_s

    # 3.2: Decompor S em fatores primos
    numero_para_fatorar = s_original
    lista_de_fatores_primos = []
    divisor = 2
    
    # Loop para encontrar os fatores
    while numero_para_fatorar > 1:
        # Checamos se o número é divisível pelo divisor atual
        if numero_para_fatorar % divisor == 0:
            # Se for, encontramos um fator! Adicionamos à lista.
            lista_de_fatores_primos.append(divisor)
            # E dividimos o número por esse fator para continuar.
            numero_para_fatorar = numero_para_fatorar // divisor
        else:
            # Se não for divisível, tentamos o próximo divisor.
            divisor = divisor + 1

    # 3.3: Montar a string final do Hash
    
    # Primeiro, criamos uma lista vazia para guardar os fatores como texto
    fatores_em_texto = []
    # Agora, passamos por cada número na nossa lista de fatores
    for fator in lista_de_fatores_primos:
        # Convertemos o número para texto e adicionamos à nova lista
        fatores_em_texto.append(str(fator))
    
    # Juntamos todos os textos da lista em uma única string
    string_f = "".join(fatores_em_texto)
    
    # Montamos o hash final
    hash_final = str(s_original) + string_f
    
    # --- Fim do cálculo do Hash ---
    
    # 3.4: Imprimir a saída formatada para o cliente atual
    print(usuario_atual)
    print(hash_final)
    print('-' * 30)