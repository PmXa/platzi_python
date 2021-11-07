''' ----------------------------------------
Hangman Game v0.3
Platzi's Intermediate-Python Course Project
By PmXa [11-2021]
---------------------------------------- '''

# ----------------------
# Dependencies
# ----------------------

from drawings import *
from os import system
import random
import unidecode

# ----------------------
# Function definitions
# ----------------------

def get_words():
    words = []
    with open("./files/words.txt","r", encoding="utf-8") as file:
        for line in file:
            words.append(line)
    return words


def process_word(word):
    processed_word = {}
    for index, element in enumerate(word):
        if not (element in processed_word):
            processed_word[element] = [index]
        else:
            processed_word[element].append(index)
    return processed_word


def print_info(life_count: int, user_guess: str):
    print(banner)
    print("Ingresa una letra: ")
    print(drawings[6 - life_count])
    print("💖"*life_count)
    print(" ".join(user_guess))

# ----------------------
# Main function & entry point 
# ----------------------

def run():
    word_list = get_words()
    original_word = random.choice(word_list)
    word = unidecode.unidecode(original_word)
    answer = process_word(word)

    guess = ["_" for i in range(len(word) - 1)]
    lives = 6

    while lives > 0:
        _ = system("clear")
        print_info(lives, guess)
        try:
            letter = input()
            if (len(letter) != 1) or (not letter.isalpha()):
                raise ValueError("¡Ingresa una letra!")
            elif letter in answer:
                for i in answer.get(letter):
                    guess[i] = letter
            else:
                lives -= 1
        except ValueError as ve:
            print(ve)
        
        if not ("_" in guess):
            _ = system("clear")
            print(drawings[-1])
            print(winning_message)
            break
        
    if lives == 0:
        _ = system("clear")
        print(banner)
        print_info(lives, guess)
        print("¡Perdiste! La respuesta era:", original_word)


if __name__ == '__main__':
    run()