import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")
window.geometry("200x300")
window.resizable(0, 0)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', ".", "/",
    "="
];

input_value = tk.StringVar()

def handle_key_press(key):
    if(key == '='):
        result = eval(input_value.get())
    elif(key == 'C'):
        result = '0'
    else:
        result = input_value.get() + key
    input_value.set(result)

window.rowconfigure((0,1,2,3), weight=1)
window.columnconfigure((0,1,2,3), weight=1)

input = ttk.Entry(master=window, justify='right', textvariable=input_value, font=('Arial, 30'))
input.grid(row=0, column=0, columnspan=4 , sticky="nsew")

row = 1
col = 0

for i in range(len(buttons)):

    if(buttons[i] == "="):
        button = ttk.Button(master=window, text= buttons[i], command= lambda x = buttons[i]: handle_key_press(x))
        button.grid(row=row, column=col, columnspan=4, sticky="nsew")
    else:
        button = ttk.Button(master=window, text= buttons[i], command= lambda x = buttons[i]: handle_key_press(x) )
        button.grid(row=row, column=col, sticky="nsew")

    col = col + 1
    if(col> 3):
        row = row + 1
        col = 0


window.mainloop()