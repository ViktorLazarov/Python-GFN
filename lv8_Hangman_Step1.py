#   _  _                                
#  | || |__ _ _ _  __ _ _ __  __ _ _ _  
#  | __ / _` | ' \/ _` | '  \/ _` | ' \ 
#  |_||_\__,_|_||_\__, |_|_|_\__,_|_||_|
#                 |___/                 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# Step 1

word_list = ["Dragonball", "JavaScript", "Python", "Programmieren"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0,len(word_list)-1)]
chosen_word_list = list(chosen_word.lower())
print(chosen_word_list)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# userGuess = input("Make a guess: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
lives = 7
wordIsFound = False
while True:
    userGuess = input("Make a guess: ").lower()
    if userGuess in chosen_word_list:
        print("Correct")
        chosen_word_list[chosen_word_list.index(userGuess)] = ' '
        print(chosen_word_list)
        for letter in chosen_word_list:
            if letter == ' ':
                wordIsFound = True
            else:
                wordIsFound = False
    else:
        print("Wrong, try again")
        print(stages[lives-1])
        lives -= 1
        
    if wordIsFound:
        print("You found all the letters.")
        break
    if lives == 0:
        print("No more lives.")
        break
    
print("Thx for playing!")

