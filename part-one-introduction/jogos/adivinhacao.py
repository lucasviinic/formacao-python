import random

print("********************************")
print("Bem vindo ao jogo da Adivinhação")
print("********************************")

numero_secreto = random.randrange(1,101)
numero_de_tentativas = 3

for rodada in range(1, numero_de_tentativas + 1):
    print(f"Rodada {rodada} de {numero_de_tentativas}")
    chute = int(input("Digite um número entre 1 e 100: "))
    print(f"Você chutou o número {chute} ee...")

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100.")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Você acertou! :)")
        break
    else:
        if maior:
            print("Você errou... O seu chute foi maior que o número secreto :(")
        else:
            print("Você errou... O seu chute foi menor que o número secreto :(")

print("Fim!")