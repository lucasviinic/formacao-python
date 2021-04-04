import random

print("********************************")
print("Bem vindo ao jogo da Adivinhação")
print("********************************")

numero_secreto = random.randrange(1,101)
numero_de_tentativas = 0
pontos = 1000

while True:
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        numero_de_tentativas = 20
        print("NÍVEL: Fácil")
        break
    elif nivel == 2:
        numero_de_tentativas = 10
        print("NÍVEL: Médio")
        break
    elif nivel == 3:
        numero_de_tentativas = 5
        print("NÍVEL: Difícil")
        break
    else:
        print("Nível invalido!")
        continue

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
        print(f"Você acertou e fez {pontos} pontos!")
        break
    else:
        if maior:
            print("Você errou... O seu chute foi maior que o número secreto :(")
        else:
            print("Você errou... O seu chute foi menor que o número secreto :(")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

print("Fim!")