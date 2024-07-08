import math

def calc_celsius_to_kelvin(userInput):
    return userInput + 273.15

def calc_celsius_to_fahrenheit(userInput):
    return (userInput * 1.8) + 32

def calc_kelvin_to_celsius(userInput):
    return userInput - 273.15

def calc_kelvin_to_fahrenheit(userInput):
    return ((userInput - 273.15) * 1.8) + 32

def calc_fahrenheit_to_celsius(userInput):
    return 1.8 * (userInput - 32)

def calc_fahrenheit_to_kelvin(userInput):
    return ((userInput - 32) * 1.8) + 273.15

def take_user_input():
    return float(input("Please enter the temperature in the chosen format: "))

#welcome screen
print("Please choose an option: ")
print("(1) Umrechnung von Celsius nach Kelvin\n(2) Umrechnung von Celsius nach Fahrenheit\n(3) Umrechnung von Kelvin nach Celsius\n(4) Umrechnung von Kelvin nach Fahrenheit\n(5) Umrechnung von Fahrenheit nach Celsius\n(6) Umrechnung von Fahrenheit nach Kelvin")
#take user choice
userChoice = input()

#based on user choice call the corresponding function

match userChoice:
    case "1": print(f"The temperature you entered was in Celsius, which is {str(round(calc_celsius_to_kelvin(take_user_input()),2))} degrees in Kelvin")
    
    case "2": print(f"The temperature you entered was in Celsius, which is {str(round(calc_celsius_to_fahrenheit(take_user_input()),2))} degrees in Fahrenheit")
    
    case "3": print(f"The temperature you entered was in Kelvin, which is {str(round(calc_kelvin_to_celsius(take_user_input()),2))} degrees in Celsius")
    
    case "4": print(f"The temperature you entered was in Kelvin, which is {str(round(calc_kelvin_to_fahrenheit(take_user_input()),2))} degrees in Fahrenheit")
    
    case "5": print(f"The temperature you entered was in Fahrenheit , which is {str(round(calc_fahrenheit_to_celsius(take_user_input()),2))} degrees in Celsius")
    
    case "6": print(f"The temperature you entered was in Fahrenheit , which is {str(round(calc_fahrenheit_to_kelvin(take_user_input()),2))} degrees in Kelvin")



