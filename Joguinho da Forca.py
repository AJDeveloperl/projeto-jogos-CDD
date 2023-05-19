import random

def escolher_palavra():
    palavras = ['Chara', 'Scarlet', 'Alpha', 'Asgore', 'Mettaton', 'Flowey', 'Napstablook']
    palavra = random.choice(palavras).upper()
    return palavra

def exibir_forca(parte_corpo):
    forca = [
        '''
          +---+
              |
              |
              |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        '''
    ]
    print(forca[parte_corpo])

def jogar_jogo_da_forca():
    print("Bem-vindo ao Jogo da Forca!")
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_incorretas = set()
    partes_corpo = 0

    while True:
        exibir_forca(partes_corpo)

        for letra in palavra:
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print('\n')

        letra = input("Digite uma letra: ").upper()

        if letra in letras_corretas or letra in letras_incorretas:
            print("Você já tentou essa letra. Tente novamente.\n")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            if letras_corretas == set(palavra):
                print("Parabéns! Você adivinhou a palavra:", palavra)
                break
        else:
            letras_incorretas.add(letra)
            partes_corpo += 1
            print("Letra incorreta. Você tem", 7 - partes_corpo, "tentativas restantes.\n")

        if partes_corpo == 7:
            exibir_forca(partes_corpo)
            print("Você perdeu! A palavra era:", palavra)
            break

    jogar_novamente = input("Deseja jogar novamente? (S/N)").upper()
    if jogar_novamente == 'S':
        jogar_jogo_da_forca()

jogar_jogo_da_forca()