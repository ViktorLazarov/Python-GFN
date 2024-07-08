import tkinter as tk

userChoice = 1

window = tk.Tk()
window.geometry("800x500")
window.title("GUI Project")

top_frame = tk.Frame(window).pack()

label1 = tk.Label(top_frame, text="Temperaturen Umrechnen", font=('Arial', 18)).pack(padx=20, pady=20)
label2 = tk.Label(top_frame, text="Wahlen Sie eine Option", font=('Arial', 16)).pack(pady=10)

options_frame = tk.Frame(window)
options_frame.grid(row=1, column=0)
#left side
left_frame = tk.Frame(options_frame, width=400, height=200)
left_frame.grid(row=0, column=0)
#Radio Buttons
tk.Radiobutton(left_frame, text="(1) Umrechnung von Celsius nach Kelvin", indicatoron = 0, width=40, padx=10, variable=userChoice, value=1).pack(anchor="w")
tk.Radiobutton(left_frame, text="(2) Umrechnung von Celsius nach Fahrenheit", indicatoron = 0, width=40, padx=10, variable=userChoice, value=2).pack(anchor="w")
tk.Radiobutton(left_frame, text="(3) Umrechnung von Kelvin nach Celsius", indicatoron = 0, width=40, padx=10, variable=userChoice, value=3).pack(anchor="w")
#right side
right_frame = tk.Frame(options_frame, width=400, height=200)
right_frame.grid(row=0, column=1)
#radio buttons
tk.Radiobutton(right_frame, text="(4) Umrechnung von Kelvin nach Fahrenheit", indicatoron = 0, width=40, padx=10, variable=userChoice, value=4).pack(anchor="w")
tk.Radiobutton(right_frame, text="(5) Umrechnung von Fahrenheit nach Celsius", indicatoron = 0, width=40, padx=10, variable=userChoice, value=5).pack(anchor="w")
tk.Radiobutton(right_frame, text="(6) Umrechnung von Fahrenheit nach Kelvin", indicatoron = 0, width=40, padx=10, variable=userChoice, value=6).pack(anchor="w")

input_frame = tk.Frame(window, width=800, height=80, bg="red")
input_frame.grid(row=2, column=0)
label3 = tk.Label(input_frame, text="Bitte geben Sie eine Temperatur ein, die der gewählten Option entspricht.", padx=10, font=('Arial', 15)).pack()

window.mainloop()