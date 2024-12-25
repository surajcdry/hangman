# Pick a random word & total life
# Show as many dashes as letters in word

import random
import os

total_life = 7
game_over = False
dash = []
word = ""
banner = '''
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/  
    '''
list_hangman = [
        '''
        _______
     |/      |
     |         
     |         
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |         
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |       | 
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \| 
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |        
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |         
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /  
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
 ____|___
 ''', '''
        _______
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      | | 
     |
 ____|___
 '''
    ]

def start():
    words = ["heaven", "computer", "hangman", "winter", "camel"]
    global word
    global total_life
    global game_over
    global dash

    word = random.choice(words)
    total_life = 7
    game_over = False
    dash = []
    for i in range(len(word)):
        dash.append("_")

start()

# Prompt user for input

# Check if user input (letter) in word
    # If yes, replace dash with chosen letter and check if all dashes gone
        # If yes, Win.
        # Else, continue to prompt.
    # If no, total_life - 1 and check if total_life == 0
        # If yes, Lose.
        # Else, continue to prompt.

while not game_over:
    os.system('clear')
    print(banner)
    print(list_hangman[7-total_life])
    print("Total life remaining:", total_life)
    print("Word: ", end="")
    print(" ".join(dash))
    print("")
    choice = input("Enter a letter: ")
    if choice in word:
        for i in range(len(word)):
            if word[i] == choice:
                dash[i] = choice
    else:
        total_life -= 1

    if "_" not in dash:
        os.system('clear')
        print(banner)
        print(list_hangman[7-total_life])
        print("You Win!\n")
        game_over = True
    elif total_life == 0:
        os.system('clear')
        print(banner)
        print(list_hangman[8])
        print("You Lose!\n")
        game_over = True

    if game_over:
        again = input("Play again? (y/n): ")
        if again.lower() == "y":
            start()