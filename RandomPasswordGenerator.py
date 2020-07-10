import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo

screen = tk.Tk()
screen.title("Random Password Generator")


def create():
    name = enter_name.get()
    password_size = int(enter_length.get())
    password = ''
    for i in range(0, password_size):
        password = password + random.choice(name)
    showinfo("Created Password", f"Your Password:{password}")


label = tk.Label(screen, text="Enter Name")
label.grid(row=0, column=0)
enter_name = tk.Entry(screen)
enter_name.grid(row=0, column=1)
label1 = tk.Label(screen, text="Enter size of Password ")
label1.grid(row=1, column=0)
enter_length = tk.Entry(screen)
enter_length.grid(row=1, column=1)
button = ttk.Button(screen, text="Show", command=create)
button.grid(row=2, column=1)
screen.mainloop()
