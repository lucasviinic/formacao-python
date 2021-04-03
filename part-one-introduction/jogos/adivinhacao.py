print("********************************")
print("Bem vindo ao jogo da Adivinhação")
print("********************************")

numero_secreto = 42
numero_de_tentativas = 3

for rodada in range(1, numero_de_tentativas + 1):
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

print("Fim!")