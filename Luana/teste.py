from collections import deque
# --- PASSO 1: CONSTRUIR O MAPA ---
# Lemos a quantidade de conexões
qc = int(input())

# Criamos nosso dicionário para o mapa
mapa_de_amigos = {}

for _ in range(qc):
    # Lemos um par de nomes
    nome1, nome2 = input().split()
    
    # Adicionamos a conexão nos dois sentidos (mão dupla)
    # Se o nome ainda não existe no mapa, criamos uma lista vazia para ele
    if nome1 not in mapa_de_amigos:
        mapa_de_amigos[nome1] = []
    if nome2 not in mapa_de_amigos:
        mapa_de_amigos[nome2] = []
    
    # Adicionamos os amigos às suas listas
    mapa_de_amigos[nome1].append(nome2)
    mapa_de_amigos[nome2].append(nome1)

# Lemos e descartamos a linha separadora '-'
input()


# --- PASSO 2: RESPONDER ÀS PERGUNTAS ---

# Loop para ler as perguntas até encontrar '* *'
while True:
    linha_pergunta = input()
    if linha_pergunta == '* *':
        break
        
    origem, destino = linha_pergunta.split()
    
    # --- Início da Lógica de Busca (BFS) para esta pergunta ---
    
    # Se a origem ou o destino nem sequer existem no mapa, não há conexão
    if origem not in mapa_de_amigos or destino not in mapa_de_amigos:
        distancia = -1 # Usamos -1 para sinalizar que não há conexão
    else:
        # Ingredientes do BFS
        fila_de_visitacao = deque([origem]) # Nossa "lista a fazer"
        distancias = {origem: 0}            # Nosso "dicionário de distâncias / visitados"
        
        encontrou_o_destino = False

        # Loop de exploração
        while fila_de_visitacao:
            pessoa_atual = fila_de_visitacao.popleft() # Pega o primeiro da fila

            if pessoa_atual == destino:
                encontrou_o_destino = True
                break # Encontramos! Podemos parar o loop.

            # Olhamos os vizinhos (amigos diretos) da pessoa atual
            for amigo in mapa_de_amigos[pessoa_atual]:
                # Se o amigo ainda não foi visitado...
                if amigo not in distancias:
                    # ...registramos sua distância e o colocamos na fila para visitar depois.
                    distancias[amigo] = distancias[pessoa_atual] + 1
                    fila_de_visitacao.append(amigo)
        
        # Depois que o loop acaba, verificamos se encontramos o destino
        if encontrou_o_destino:
            distancia = distancias[destino]
        else:
            distancia = -1

    # --- Fim da Lógica de Busca ---
    
    # Imprime o resultado no formato pedido
    print(f"{origem}-{destino} = ", end="")
    if distancia == -1:
        print("sem conexao")
    else:
        print(distancia)