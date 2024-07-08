import tkinter as tk


def calc_celsius_to_kelvin(user_input):
    return user_input + 273.15

def calc_celsius_to_fahrenheit(user_input):
    return (user_input * 1.8) + 32

def calc_kelvin_to_celsius(user_input):
    return user_input - 273.15

def calc_kelvin_to_fahrenheit(user_input):
    return ((user_input - 273.15) * 1.8) + 32

def calc_fahrenheit_to_celsius(user_input):
    return 1.8 * (user_input - 32)

def calc_fahrenheit_to_kelvin(user_input):
    return ((user_input - 32) * 1.8) + 273.15   

def calculate():
    global output, label4
    if user_choice.get() == 0 or user_input.get() == "":
        print("Please choose an option and enter a value")
    else:
        match user_choice.get():
            case 1: output.set("The temperature you entered was in Celsius,\n which is " +  str(round(calc_celsius_to_kelvin(float(user_input.get())),2)) +  " degrees in Kelvin")
            
            case 2: output.set("The temperature you entered was in Celsius,\n which is " + str(round(calc_celsius_to_fahrenheit(float(user_input.get())),2)) + " degrees in Fahrenheit")
            
            case 3: output.set("The temperature you entered was in Kelvin,\n which is " + str(round(calc_kelvin_to_celsius(float(user_input.get())),2)) + " degrees in Celsius")
            
            case 4: output.set("The temperature you entered was in Kelvin,\n which is " + str(round(calc_kelvin_to_fahrenheit(float(user_input.get())),2)) + " degrees in Fahrenheit")
            
            case 5: output.set("The temperature you entered was in Fahrenheit,\n which is "+ str(round(calc_fahrenheit_to_celsius(float(user_input.get())),2)) + " degrees in Celsius")
            
            case 6: output.set("The temperature you entered was in Fahrenheit,\n which is " + str(round(calc_fahrenheit_to_kelvin(float(user_input.get())),2)) + " degrees in Kelvin")
        label4 = tk.Label(window, text=output.get(), font=("Areal", 20))
        label4.grid(row=4,column=0, columnspan=2)

def reset():
    user_choice.set(0)
    user_input.set("")
    output.set("")
    label4.destroy()



window = tk.Tk()
window.geometry("900x700")
window.title("GUI Project")
window.columnconfigure(0, weight=1, uniform='a')
window.columnconfigure(1, weight=1, uniform='a')
window.rowconfigure(0, weight=5, uniform='a')
window.rowconfigure(1, weight=2, uniform='a')
window.rowconfigure(2, weight=2, uniform='a')
window.rowconfigure(3, weight=2, uniform='a')
window.rowconfigure(4, weight=15, uniform='a')


user_choice = tk.IntVar()
user_choice.set(0)
user_input = tk.StringVar()
output = tk.StringVar()


label1 = tk.Label(window, text="Temperatur Converter", font=("Areal", 18), pady=20).grid(row=0,column=0, columnspan=2, sticky="n")
label2 = tk.Label(window, text="Please choose an option:", font=("Areal", 16), pady=10).grid(row=0,column=0, columnspan=2, sticky='s')
label3 = tk.Label(window, text="Please enter a temperature below:", font=("Areal", 14), pady=5).grid(row=4,column=0, columnspan=2, sticky='n')

entry = tk.Entry(window, textvariable=user_input, font=("Areal", 16)).grid(row=0,column=0, columnspan=2, rowspan=5)

radio1 = tk.Radiobutton(window, 
                        text="(1) Umrechnung von Celsius nach Kelvin", 
                        indicatoron = 0,
                        font=("Areal", 16), 
                        variable=user_choice, 
                        value=1, bg="grey").grid(row=1, 
                                                column=0, 
                                                sticky='nsew')
radio2 = tk.Radiobutton(window, 
                        text="(2) Umrechnung von Celsius nach Fahrenheit", 
                        indicatoron = 0,
                        font=("Areal", 16), 
                        variable=user_choice, 
                        value=2, bg="grey").grid(row=1, 
                                                column=1, 
                                                sticky='nsew')
radio3 = tk.Radiobutton(window, 
                        text="(3) Umrechnung von Kelvin nach Celsius", 
                        indicatoron = 0,
                        font=("Areal", 16), 
                        variable=user_choice, 
                        value=3, bg="grey").grid(row=2, 
                                                column=0, 
                                                sticky='nsew')
radio4 = tk.Radiobutton(window, 
                        text="(4) Umrechnung von Kelvin nach Fahrenheit", 
                        indicatoron = 0,
                        font=("Areal", 16), 
                        variable=user_choice, 
                        value=4, bg="grey").grid(row=2, 
                                                column=1, 
                                                sticky='nsew')
radio5 = tk.Radiobutton(window, 
                        text="(5) Umrechnung von Fahrenheit nach Celsius", 
                        indicatoron = 0,
                        font=("Areal", 16), 
                        variable=user_choice, 
                        value=5, bg="grey").grid(row=3, 
                                                column=0, 
                                                sticky='nsew')
radio6 = tk.Radiobutton(window, 
                        text="(6) Umrechnung von Fahrenheit nach Kelvin", 
                        indicatoron = 0,
                        font=("Areal", 16), 
                        variable=user_choice, 
                        value=6, bg="grey").grid(row=3, 
                                                column=1, 
                                                sticky='nsew')

button = tk.Button(window, 
                    text="Calculate!", 
                    font=("Areal", 16),
                    bg="#b3ffff",
                    command=calculate).grid(row=1, column=0, rowspan=4)

reset_button = tk.Button(window, 
                    text="Reset!", 
                    font=("Areal", 16),
                    bg="#b3ffff",
                    command=reset).grid(row=1, column=1, rowspan=4)

window.mainloop()