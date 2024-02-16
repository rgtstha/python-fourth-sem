import tkinter as tk
from tkinter import ttk
from tkinter import font

window = tk.Tk()
window.title("This is my first GUI Program")
window.minsize(width=500, height=400)

# Label first
label_first = ttk.Label(master=window, text="Num 1:")
label_first.grid(row=0, column=0, padx=10)

# Textfield
text_field_first =  ttk.Entry(master=window)
text_field_first.grid(row=0, column=1, pady=10, padx=10)


#label second
label_second = ttk.Label(master=window, text="Num 2:")
label_second.grid(row=1, column=0, padx=10)

text_field_second =  ttk.Entry(master=window)
text_field_second.grid( row= 1, column= 1, pady=10, padx=10)

#Button
def my_button_handler():
    num_1 =  text_field_first.get()
    num_2 =  text_field_second.get()

    sum = int(num_1) + int(num_2)
    print("The sum is", sum)
    result_label.configure(text= "Result =" + str(sum))


my_button = ttk.Button(master=window, text="Add", command=my_button_handler)
my_button.grid(row=2, column=1, pady=10,sticky="w", padx=10)

result_label = ttk.Label(master=window, text = "Result=", font=font.Font(size=25))
result_label.grid(row=3, column=0, pady=10, columnspan=2)
window.mainloop()