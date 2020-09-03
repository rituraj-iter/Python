import random
from tkinter import *
from tkinter import messagebox
text = "abcedefghijklmnopqrstuvwxyz0123456789"
root = Tk()
root.title("Captcha Generator")
root.geometry("200x200")
captcha_var = StringVar()
input = StringVar()


def captcha_setter():
    s = random.choices(text, k=8)
    captcha_var.set(''.join(s))


def check():
    if captcha_var.get() == input.get():
        messagebox.showinfo("Success", "Correct")
    else:
        messagebox.showerror("Error", "Incorrect")
    captcha_setter()


Label(root, textvariable=captcha_var, font="Arial 18 bold").pack()
Entry(root, textvariable=input, font="Arial 12 bold").pack(ipady=5)
Button(root, command=check, text="Check", font="Arial 12").pack()
captcha_setter()
root.mainloop()
