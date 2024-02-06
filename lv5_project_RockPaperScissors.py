import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Schreiben Sie Ihren Programmcode unter dieser Zeile 👇
choice = [scissors, paper, rock]
userScore = 0
computerScore = 0

while True:
    computerChoice = choice[random.randint(0, 2)]
    userChoise = input("Enter your choice (rock, paper, scissors): ")
    
    if userChoise == 'rock':
        if computerChoice == rock:
            print(computerChoice)
            print("It's a tie!")
        elif computerChoice == scissors:
            print(computerChoice)
            print("You Win!")
            userScore+= 1
        else:
            print(computerChoice)
            print("You Lose!")
            computerScore+= 1
    elif userChoise == 'scissors':
        if computerChoice == scissors:
            print(computerChoice)
            print("It's a tie!")
        elif computerChoice == paper:
            print(computerChoice)
            print("You Win!")
            userScore+= 1
        else:
            print(computerChoice)
            print("You Lose!")
            computerScore+= 1
    else:
        if computerChoice == paper:
            print(computerChoice)
            print("It's a tie!")
        elif computerChoice == rock:
            print(computerChoice)
            print("You Win!")
            userScore+= 1
        else:
            print(computerChoice)
            print("You Lose!")
            computerScore+= 1
            
    if userScore == 3:
        print("User Wins!")
        break
    elif computerScore == 3:
        print("Computer Wins!")
        break
        
print("Thx for playing")
# print(computerChoice)
# print(userChoise)