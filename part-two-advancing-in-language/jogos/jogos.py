import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("****** Escolha o seu jogo ******")
    print("********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual o jogo? "))

    while True:
        if jogo == 1:
            forca.jogar()
            break
        elif jogo == 2:
            adivinhacao.jogar()
            break
        else:
            print("Opção invalida")
            continue

if __name__ == '__main__':
    escolhe_jogo()