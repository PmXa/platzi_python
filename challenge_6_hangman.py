''' ----------------------------------------
Hangman Game v0.1
Platzi's Intermediate-Python Course Project
By PmXa [11-2021]
---------------------------------------- '''

# ----------------------
# Dependencies
# ----------------------

from drawings import *
import random
from os import system

# ----------------------
# Function definitions
# ----------------------

def get_words():
    words = []
    with open("./files/words.txt","r", encoding="utf-8") as file:
        for line in file:
            words.append(line)
    return words


def print_info(life_count: int, user_guess: str):
    print(drawings[6 - life_count])
    print("💖"*life_count)
    print(" ".join(user_guess))
    print("Ingresa una letra: ")

# ----------------------
# Main function & entry point 
# ----------------------

def run():
    word_list = get_words()
    word = random.choice(word_list)

    answer = {}
    for index, element in enumerate(word[:-1]):
        if not (element in answer):
            answer[element] = [index]
        else:
            answer[element].append(index)

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
            print("¡Ganaste!")
            break
        
    if lives == 0:
        _ = system("clear")
        print_info(lives, guess)
        print("¡Perdiste! La respuesta era:", word)


if __name__ == '__main__':
    run()