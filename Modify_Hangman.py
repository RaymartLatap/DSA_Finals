import random

with open('wordlist.txt',  'r') as f:
    words = f.readlines()

# Function to print the stickman
def print_man(mistakes):
    if mistakes == 0:
        print("_____")
        print("|   |")
        print("|")
        print("|")
        print("|")
        print("|")
    elif mistakes == 1:
        print("_____")
        print("|   |")
        print("|   O")
        print("|")
        print("|")
        print("|")
    elif mistakes == 2:
        print("_____")
        print("|   |")
        print("|   O")
        print("|   |")
        print("|")
        print("|")
    elif mistakes == 3:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|")
        print("|")
        print("|")
    elif mistakes == 4:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|")
        print("|")
    elif mistakes == 5:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|  /")
        print("|")
    else:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|  / \\")
        print("|")

# Function to get a random word from the list of words
def get_word():
    return random.choice(words)[:-1]

# Function to get the player's guess
def get_guess():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single letter.")

# Function to check if the guess is correct
def check_guess(word, guess, correct_guesses):
    if guess in word:
        correct_guesses.add(guess)
        return True
    else:
        return False

# Function to print the word with blanks for unguessed letters
def print_word(word, correct_guesses):
    for letter in word:
        if letter in correct_guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

# Function to play the game
def play_game():
    print("Welcome to Hangman!\n")
    level = input("Select your level (Easy/Medium/Hard): ")
    if level.lower() == "easy":
        max_mistakes = 9
    elif level.lower() == "medium":
        max_mistakes = 7
    else:
        max_mistakes = 6
    word = get_word()
    correct_guesses = set()
    mistakes = 0
    while mistakes < max_mistakes:
        print_man(mistakes)
        print_word(word, correct_guesses)
        guess = get_guess()
        if check_guess(word, guess, correct_guesses):
            print("Correct! ")
        else:
            print("Trials left: ", max_mistakes - mistakes)
            print("Incorrect!")
            mistakes += 1
        if set(word) == correct_guesses:
            print_man(mistakes)
            print_word(word, correct_guesses)
            print('\n Already Guessed!!')
            break
        if mistakes == max_mistakes:
            print_man(mistakes)
            print("\nGame Over!!, You lost the game")
            print("Correct word was: ", word)
            return
            
# Print a clue if the player has used half of the trials
        if mistakes == max_mistakes // 2:
            print(f"Clue: The word starts with {word[0]}.")
            
    print_man(mistakes)
    print_word(word, correct_guesses)
    
#Start the Game    
play_game()