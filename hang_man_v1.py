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

# Função de incialização do jogo
def start():
    clear_screen()
    print('\nBem-vindo(a) ao jogo da forca.\nSeu objetivo é advinhar a palavra dentro do limite de tentativas.\n')

    # Lista de palavras
    words = ['banana', 'laranja', 'morango', 'abacaxi', 'uva', 'melancia', 'kiwi', 'manga']

    # Palavra oculta
    word = random.choice(words)
    hidden_letters = ['_' for _ in word]

    # Número de chances
    chances = 6

    # Lista de letras erradas
    wrong_letters = []

    while chances > 0:
        print(" ".join(hidden_letters))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(wrong_letters))

        # Tentativa
        attempt = input("\nDigite uma letra: ").lower()

        if attempt in wrong_letters:
            print("\nTente uma letra diferente!")
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

if __name__ == '__main__':
    start()
