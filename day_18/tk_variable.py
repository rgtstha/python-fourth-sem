import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Demo")
window.geometry("300x200")


my_variable = tk.StringVar()
another_varilable = tk.IntVar()
another_variable_1 = tk.BooleanVar()


entry = ttk.Entry(textvariable=my_variable)
entry.pack(pady= 10)


entry_label = ttk.Label(textvariable= my_variable)
entry_label.pack(pady= 10)

window.mainloop()