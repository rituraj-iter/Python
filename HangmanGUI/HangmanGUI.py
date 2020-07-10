import random
from tkinter import *
from tkinter import messagebox

run = True
while run:
    root = Tk()
    root.geometry('1000x1000')
    root.title('HANGMAN')
    root.config(bg='Black')
    num_cor_inp = 0
    num_incor_inp = 0
    word_pos = random.randint(0, 1000)
    word_dir = open('words.txt', 'r')
    words = word_dir.readlines()
    word_selected = words[word_pos].strip('\n')
    x = 200
    for i in range(0, len(word_selected)):
        x = x + 50
        exec('d{}=Label(root,text="_",bg="Red",font=("arial",36))'.format(i))
        exec('d{}.place(x={},y={})'.format(i, x, 400))
    letters_icon = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    for let in letters_icon:
        exec('{}=PhotoImage(file="{}.png\")'.format(let, let))
    hangman_position = ['hangman1', 'hangman2', 'hangman3', 'hangman4', 'hangman5', 'hangman6', 'hangman7']
    for hangman in hangman_position:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman, hangman))
    button = [['b1', 'a', 30, 500], ['b2', 'b', 100, 500], ['b3', 'c', 170, 500], ['b4', 'd', 240, 500],
              ['b5', 'e', 310, 500], ['b6', 'f', 380, 500], ['b7', 'g', 450, 500], ['b8', 'h', 520, 500],
              ['b9', 'i', 590, 500], ['b10', 'j', 660, 500], ['b11', 'k', 730, 500], ['b12', 'l', 800, 500],
              ['b13', 'm', 870, 500], ['b14', 'n', 30, 600], ['b15', 'o', 100, 600], ['b16', 'p', 170, 600],
              ['b17', 'q', 240, 600], ['b18', 'r', 310, 600], ['b19', 's', 380, 600], ['b20', 't', 450, 600],
              ['b21', 'u', 520, 600], ['b22', 'v', 590, 600], ['b23', 'w', 660, 600], ['b24', 'x', 730, 600],
              ['b25', 'y', 800, 600], ['b26', 'z', 870, 600]]

    for but in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="Green",activebackground="Yellow",font=10,'
             'image={})'.format(
            but[0], but[1], but[0], but[1]))
        exec('{}.place(x={},y={})'.format(but[0], but[2], but[3]))

    han = [['pos1', 'hangman1'], ['pos2', 'hangman2'], ['pos3', 'hangman3'], ['pos4', 'hangman4'], ['pos5', 'hangman5'],
           ['pos6', 'hangman6'], ['pos7', 'hangman7']]
    for pos in han:
        exec('{}=Label(root,bg="Green",image={})'.format(pos[0], pos[1]))
    pos1.place(x=250, y=0)


    def close():
        global run
        choice = messagebox.askyesno('Warning', 'Do you want to exit the game')
        if choice:
            run = False
            root.destroy()


    exit_img = PhotoImage(file='exit.png')
    exit_pos = Button(root, bd=0, command=close, bg="Green", activebackground="Yellow", font=10, image=exit_img)
    exit_pos.place(x=770, y=10)


    def check(letter, button):
        global num_cor_inp, num_incor_inp, run
        exec('{}.destroy()'.format(button))
        if letter in word_selected:
            for i in range(0, len(word_selected)):
                if word_selected[i] == letter:
                    num_cor_inp += 1
                    exec('d{}.config(text="{}")'.format(i, letter.upper()))
            if num_cor_inp == len(word_selected):
                answer = messagebox.askyesno('Game over', 'You won\nPlay again')
                if answer:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        else:
            num_incor_inp += 1
            exec('pos{}.destroy()'.format(num_incor_inp))
            exec('pos{}.place(x={},y={})'.format(num_incor_inp + 1, 300, 0))
            if num_incor_inp == 6:
                answer = messagebox.askyesno('Game over', 'You lost\nPlay again')
                if answer:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()


    root.mainloop()
