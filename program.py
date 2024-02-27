import requests
import os
import time
import sys
api_url = 'https://random-word-api.herokuapp.com/word'


response = requests.get(api_url)

get_word = response.text
get_word_cleaned = get_word.strip('[""]')
i = 0

def valid_input(prompt='Enter your guess: '):
    while True:
        user_input = input(prompt).strip()

        if user_input.isdigit() or len(user_input) != 1:
            print('Bad input, try again')
        else:
            return True and user_input


def clear_console():
    os.system("clear || cls")



def end_game():
    print('Congratulations, you won!')
    print(f'The hidden word was: {get_word_cleaned} ')
    for i in range(5, 0, -1):
        print(f'Exiting program in {i} seconds', end = ' \r')
        sys.stdout.flush()
        time.sleep(1)

def game_over():
    clear_console()
    print(f'Game over, the hidden word was: {get_word_cleaned}')
    print("   sss     ")
    print("  (x x)    ")
    print("o-- O --o  ")
    print("   / \     ")
    print("  /   \    ")


def the_hanged_man(attempts):
    match attempts:
        case 1:
            print("   sss      ")
        case 2:
            print("   sss      ")
            print("  (o o)     ")
        case 3:
            print("   sss      ")
            print("  (o o)     ")
            print("    O       ")
        case 4:
            print("   sss     ")
            print("  (o o)    ")
            print("    O      ")
            print("o-- O      ")
        case 5:
            print("   sss     ")
            print("  (o o)    ")
            print("    O      ")
            print("o-- O      ")
            print("o-- O --o  ")
        case 6:
            print("   sss     ")
            print("  (o o)    ")
            print("    O      ")
            print("o-- O      ")
            print("o-- O --o  ")
            print("   / \     ")
        case 7:
            print("   sss     ")
            print("  (x x)    ")
            print("o-- O --o  ")
            print("   / \     ")
            print("  /   \    ")



def hangman():
    attempts = 0
    game_won = False

    list = ['_'] * len(get_word_cleaned)
    underscore_checker = list.count('_')

    clear_console()
    print('Welcome to Hangman')
    print('The goal of the game is to guess what the hidden word is')
    time.sleep(5)
    clear_console()

    #print(get_word_cleaned)





    print(f'You have {7-attempts} attempts left\n') 
    print(list)


    while attempts <= 7 and not game_won:

        #gamestate_checker
        if underscore_checker == 0:
            game_won = True
            clear_console()
            end_game()
            break

        guess = valid_input()
        user_guesses = [guess]

        if str(guess) not in get_word_cleaned:
            print("Wrong guess, try again")
            attempts += 1
            the_hanged_man(attempts)
            if str(guess) in user_guesses:


                print('You have already guessed this character')
        else:
            char_indices = [index for index, char in enumerate(get_word_cleaned) if char == guess]

            for index in char_indices:
                list[index] = guess
            char_index = get_word_cleaned.index(guess)
            list[char_index] = guess
            underscore_checker = list.count('_')
            print(list)
    game_over()



hangman()


