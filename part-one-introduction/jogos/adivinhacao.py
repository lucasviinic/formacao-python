print("********************************")
print("Bem vindo ao jogo da Adivinhação")
print("********************************")

numero_secreto = 42
rodada = 1
numero_de_tentativas = 3

while rodada <= numero_de_tentativas:
    print(f"Rodada {rodada} de {numero_de_tentativas}")
    chute = int(input("Digite o seu chute: "))
    print(f"Você chutou o número {chute} ee...")

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Você acertou! :)")
    else:
        if maior:
            print("Você errou... O seu chute foi maior que o número secreto :(")
        else:
            print("Você errou... O seu chute foi menor que o número secreto :(")

    rodada += 1

print("Fim!")