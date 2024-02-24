import requests
import os
import time
import sys
api_url = 'https://random-word-api.herokuapp.com/word'


response = requests.get(api_url)

get_word = response.text
get_word_cleaned = get_word.strip('[""]')
i = 0

def valid_input(prompt='Skriv din gissning här: '):
    while True:
        user_input = input(prompt).strip()

        if user_input.isdigit() or len(user_input) != 1:
            print('Bad input, try again')
        else:
            print('good input') 
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


""""

print("   sss      ")
print("  (o o)    ")
print("o-- O --o  ")
print("   / \     ")
print("  /   \    ")
print(get_word_cleaned)
"""


def hangman():
    attempts = 0
    game_won = False

    list = ['_'] * len(get_word_cleaned)
    underscore_checker = list.count('_')

    print('Welcome to Hangman')
    print('The goal of the game is to guess what the hidden word is')
    time.sleep(5)
    clear_console()

    print(get_word_cleaned)





    print(f'You have {7-attempts} attempts left')
    print(f'Number of _ :{underscore_checker}')    
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

        if str(guess) in user_guesses:
            clear_console()
            print()
            print('You have already guessed this character')

        if str(guess) not in get_word_cleaned:
            print("Wrong guess, try again")
            attempts += 1
        else:
            char_indices = [index for index, char in enumerate(get_word_cleaned) if char == guess]

            for index in char_indices:
                list[index] = guess
            char_index = get_word_cleaned.index(guess)
            char_index2 = []
            list[char_index] = guess
            #print(f'Guess was found at index pos {char_index}')

            underscore_checker = list.count('_')
            print(list)
    print('SLUT :D')
    clear_console()


hangman()


