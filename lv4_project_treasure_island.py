print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
import random
import sys

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

step_one = ['ok','Fall into a hole.\nGame Over!']
step_two_wait = ['ok','Eaten by beasts.\nGame Over!']
step_two_swim = ['ok','Attacked by trout.\nGame Over!']
step_three = ['ok','Eaten by beasts.\nGame Over!', 'Burned by fire.\nGame Over!']

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

player_move = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": \n')

if player_move == 'left' or player_move == 'right':
        if 'ok' != step_one[random.randint(0, 1)]:
            print(step_one[1])
            sys.exit()
        else:
            player_move_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.: \n')
            match player_move_2:
                case 'swim':
                    if step_two_swim[random.randint(0, 1)] != 'ok':
                        print(step_two_swim[1])
                        sys.exit()
                    else:
                        player_move_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: \n")
                        if player_move_3 == 'Red' or player_move_3 == 'Blue' or player_move_3 =='Yellow':
                            if step_three[random.randint(0, 2)] != 'ok':
                                print(step_three[random.randint(1, 2)])
                                sys.exit()
                            else:
                                print("You Win!")
                                sys.exit()
                        else:
                            print("Game Over")
                            sys.exit()
                            
                case 'wait':
                    if step_two_wait[random.randint(0, 1)] != 'ok':
                        print(step_two_wait[1])
                        sys.exit()
                    else:
                        player_move_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: \n")
                        if player_move_3 == 'Red' or player_move_3 == 'Blue' or player_move_3 =='Yellow':
                            if step_three[random.randint(0, 2)] != 'ok':
                                print(step_three[random.randint(1, 2)])
                                sys.exit()
                            else:
                                print("You Win!")
                                sys.exit()
                        else:
                            print("Game Over")
                            sys.exit()
else:
    print("Game Over")