# Projeto 1 - Desenolvimento de Game em Linguagem Python - Versão 1 (https://www.datascienceacademy.com.br/course/fundamentos-de-linguagem-python-para-analise-de-dados-e-data-science)

import random

from os import system, name

# Função para limpar a tela de acordo com o OS
def clear_screen():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')


# Função da forca
def gallow(chances):
    stages = [
    '''
        _________
        |       |
        |       o
        |      /|\\
        |       |
        |      / \\
    ----------------
    ''',
    '''
        _________
        |       |
        |       o
        |      \\|/
        |       |
        |      /
    ----------------
    ''',
    '''
        _________
        |       |
        |       o
        |      \\|/
        |       |
        |      
    ----------------
    ''',
    '''
        _________
        |       |
        |       o
        |      \\|/
        |       
        |      
    ----------------
    ''',
    '''
        _________
        |       |
        |       o
        |      \\|
        |      
        |      
    ----------------
    ''',
    '''
        _________
        |       |
        |       o
        |       |
        |      
        |      
    ----------------
    ''',
    '''
        _________
        |       |
        |       o
        |      
        |       
        |      
    ----------------
    ''',
    '''
        _________
        |       |
        |       
        |      
        |       
        |      
    ----------------
    '''
    ]
    return stages[chances]


# Função da Interface
def ui(chances, hidden_letters, wrong_letters):
    clear_screen()
    print('Bem-vindo(a) ao jogo da forca.\nSeu objetivo é advinhar a palavra dentro do limite de tentativas.\n')
    print(gallow(chances))
    print("\t", " ".join(hidden_letters))
    print("\nChances restantes:", chances)
    print("Letras erradas:", " ".join(wrong_letters))


# Função de incialização do jogo
def start():
    # Lista de palavras
    words = ['banana', 'laranja', 'morango', 'abacaxi', 'uva', 'melancia', 'kiwi', 'manga']

    # Palavra oculta
    word = random.choice(words)
    hidden_letters = ['_' for _ in word]

    # Número de chances
    chances = 7

    # Lista de letras erradas
    wrong_letters = []

    while chances > 0:
        ui(chances, hidden_letters, wrong_letters)

        # Tentativa
        attempt = input("\nDigite uma letra: ").lower()

        if attempt in wrong_letters or len(attempt) > 1:
            print("\nTente novamente")
            continue

        if attempt in word:
            index = 0
            for letter in word:
                if attempt == letter:
                    hidden_letters[index] = letter
                index += 1
        else:
            chances -= 1
            wrong_letters.append(attempt)

        if '_' not in hidden_letters:
            print("\nVocê venceu, a palavra era: ", word)
            break
        elif chances == 0:
            ui(chances, hidden_letters, wrong_letters)
            print("\nVocê perdeu! :( a palavra era: ", word)


if __name__ == '__main__':
    while True:
        start()
        choice = input('''
Deseja iniciar um novo jogo?
    1. Sim
    2. Não
        '''
        )
        if int(choice) == 1:
            continue
        else:
            input("Obrigado por jogar!")
            break
