def jogar():
    print("********************************")
    print("** Bem vindo ao jogo da Forca **")
    print("********************************")

    palavra_secreta = "python".lower()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = input("Qual o seu chute?: ")
        chute = chute.strip().lower()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!!")
    else:
        print("Você foi enforcado!!")

    print("Fim do jogo!!")

if __name__ == '__main__':
    jogar()