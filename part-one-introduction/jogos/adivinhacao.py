print("********************************")
print("Bem vindo ao jogo da Adivinhação")
print("********************************")

numero_secreto = 42
chute = int(input("Digite o seu chute: "))
print(f"Você chutou o número {chute} ee...")

if chute == numero_secreto:
    print("Você acertou! :)")
else:
    print("Você errou... :(")

print("Fim!")