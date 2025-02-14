import random

def jogar_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        
        if palpite < numero_secreto:
            print("O número é maior! Tente novamente.")
        elif palpite > numero_secreto:
            print("O número é menor! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break


jogar_adivinhacao()
