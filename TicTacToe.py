base = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
gg = True
winner = None
cp = "X"


def display_base():
    print(base[0] + " | " + base[1] + " | " + base[2])
    print(base[3] + " | " + base[4] + " | " + base[5])
    print(base[6] + " | " + base[7] + " | " + base[8])


def game_play():
    display_base()
    while gg:
        turn(cp)
        game_completed()
        change_player()
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner is None:
        print("Tie.")


def turn(player):
    print(player + " 's turn.")
    pos = input("choose any position from 1-9.\n")
    val = False
    while not val:
        while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos = input("choose a position from 1-9.\n")
        pos = int(pos) - 1
        if base[pos] == " ":
            val = True
        else:
            print("Already occupied try different position.")
    base[pos] = player
    display_base()


def game_completed():
    check_winner()
    check_tie()


def check_winner():
    global winner
    row = row_check()
    col = col_check()
    dia = dia_check()
    if row:
        winner = row
    elif col:
        winner = col
    elif dia:
        winner = dia
    else:
        winner = None
    return


def row_check():
    global gg
    row1 = base[0] == base[1] == base[2] != " "
    row2 = base[3] == base[4] == base[5] != " "
    row3 = base[6] == base[7] == base[8] != " "
    if row1 or row2 or row3:
        gg = False
    if row1:
        return base[0]
    elif row2:
        return base[3]
    elif row3:
        return base[6]
    return


def col_check():
    global gg
    col1 = base[0] == base[3] == base[6] != " "
    col2 = base[1] == base[4] == base[7] != " "
    col3 = base[2] == base[5] == base[8] != " "
    if col1 or col2 or col3:
        gg = False
    if col1:
        return base[0]
    elif col2:
        return base[1]
    elif col3:
        return base[2]
    return


def dia_check():
    global gg
    dia1 = base[0] == base[4] == base[8] != " "
    dia2 = base[6] == base[4] == base[2] != " "
    if dia1 or dia2:
        gg = False
    if dia1:
        return base[0]
    elif dia2:
        return base[6]
    return


def check_tie():
    global gg
    if " " not in base:
        gg = False
    return


def change_player():
    global cp
    if cp == "X":
        cp = "O"
    elif cp == "O":
        cp = "X"
    return


game_play()
