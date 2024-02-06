#   ___                              _    ___                       _           
#  | _ \__ _ _______ __ _____ _ _ __| |  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
#  |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
#  |_| \__,_/__/__/\_/\_/\___/_| \__,_|  \___\___|_||_\___|_| \__,_|\__\___/_|  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                            

# Password Generator

# Erstellen Sie ein Programm, das ein Passwort für sie generiert.
# Es soll dabei nach der Anzahl der Buchstaben,
# der Anzahl der Symbole
# und der Anzahl der Ziffern fragen, die in dem Passwort enthalten sein sollen.
# Das Programm wählt dann zufällig die entsprechenden Zeichen aus den zugehörigen Listen aus
# und kombiniert diese zu einem Passwort

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

userPassword = []
# Schwierigkeitsgrad: Normal - Keine Zufällige Anordnung:
# -> 4 Buchstaben, 2 Symbole, 2 Ziffern = JduE&!91
for i in range(nr_letters):
    userPassword.append(letters[random.randint(0,len(letters)-1)])
    
for i in range(nr_symbols):
    userPassword.append(symbols[random.randint(0,len(symbols)-1)])
    
for i in range(nr_numbers):
    userPassword.append(numbers[random.randint(0,len(numbers)-1)])

print(f"Easy Mode: {''.join(userPassword)}")
print("************************************************")
# Schwierigkeitsgrad: Schwer - Zufällige Anordnung aller Zeichen:
# -> 4 Buchstaben, 2 Symbole, 2 Ziffern = g^2jk8&P
passwordLength = nr_letters+nr_numbers+nr_symbols
userPassword2 = [' ' for i in range(passwordLength)]
#generate letters at random(free) places
i = 1
while i <= nr_letters:
    randomPosition = random.randint(0,passwordLength-1)
    if userPassword2[randomPosition] == ' ':
        userPassword2[randomPosition] = letters[random.randint(0,len(letters)-1)]
        i += 1
#generate symbols at random(free) places
j = 1
while j <= nr_symbols:
    randomPosition = random.randint(0,passwordLength-1)
    if userPassword2[randomPosition] == ' ':
        userPassword2[randomPosition] = symbols[random.randint(0,len(symbols)-1)]
        j += 1
#generate numbers at random(free) places
k = 1
while k <= nr_numbers:
    randomPosition = random.randint(0,passwordLength-1)
    if userPassword2[randomPosition] == ' ':
        userPassword2[randomPosition] = numbers[random.randint(0,len(numbers)-1)]
        k += 1        
print(f"Hard Mode: {''.join(userPassword2)}")


