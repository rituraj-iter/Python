from tkinter import *
from tkinter import messagebox
import pyautogui
import os
root = Tk()
time = IntVar()
time.set(1)


def screen_shot():
    timeleft = time.get()
    if timeleft > 0:
        timeleft -= 1
        time.set(timeleft)
        root.after(1000, screen_shot)
    else:
        s = pyautogui.screenshot()
        s.save(os.getcwd()+"\screenshot.png")
        messagebox.showinfo("Screenshot", "Screenshot Saved")


label = Label(root, textvariable=time, fg="red")
label.pack
Button(root, text=f"Take screen shot", command=screen_shot).pack()
root.mainloop()
