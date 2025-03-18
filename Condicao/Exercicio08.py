print("Bem-vindo à aventura!")

escolha = input("Você está em uma floresta escura. O que você faz? (entrar / fugir): ").lower()

if escolha == "entrar":
    print("Você entrou na floresta e viu um rio. Você pode atravessá-lo ou procurar uma ponte.")
    ponte_ou_nadar = input("O que você faz? (atravessar / procurar ponte): ").lower()
    
    if ponte_ou_nadar == "atravessar":
        print("Você nadou até o outro lado e encontrou um tesouro escondido! Parabéns!")
    elif ponte_ou_nadar == "procurar ponte":
        print("Você encontrou uma ponte e cruzou com segurança. No final, encontrou um vilarejo amigável!")
    else:
        print("Opção inválida. Você ficou perdido na floresta.")
    
elif escolha == "fugir":
    print("Você fugiu rapidamente da floresta, mas acabou encontrando um abrigo seguro.")
    descansar = input("Você quer descansar agora? (sim / nao): ").lower()
    
    if descansar == "sim":
        print("Você descansou e recuperou suas forças. Agora está pronto para novas aventuras!")
    elif descansar == "nao":
        print("Você decidiu continuar explorando. Logo encontrou uma cidade cheia de pessoas amigáveis!")
    else:
        print("Opção inválida. Você ficou em dúvida sobre o que fazer e acabou indo para casa.")
    
else:
    print("Opção inválida. Você ficou parado e nada aconteceu.")
