python
enforcou = False
acertou = False
palavra_secreta = "exemplo"  # Defina a palavra secreta aqui

while not enforcou and not acertou:
    chute = input('Qual a letra? ')
    chute = chute.strip()
    index = 0
    
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            print(f'Encontrei a letra {letra} na posição {index}')
        index += 1  
    
    print('Jogando...')
    

print('Fim de jogo...')