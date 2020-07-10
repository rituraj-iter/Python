import random


def main():
    play_game = True

    while play_game:

        words = ["test", "rescue", "interfere", "light",
                 "woozy", "fetch", "wrong", "bruise"]

        word_selected = random.choice(words).lower()
        letter_guessed = []
        word_guessed = []
        for letter in word_selected:
            word_guessed.append("-")

        hangman = (
            """             -----
            |   |
            |
            |
            |
            |
            |
            |
            |
            --------""",
            """             -----
            |   |
            |   0
            |   
            |
            | 
            |
            |
            |
            --------""",
            """             -----
            |   |
            |   0
            |  -+-
            |
            |
            |
            |
            |
            --------""",
            """             -----
            |   |
            |   0
            | /-+-
            |
            |
            |
            |
            |
            --------""",
            """-----
            |   |
            |   0
            | /-+-\ 
            |
            |
            |
            |
            |
            --------""",
            """             -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |
            |
            |
            |
            --------""",
            """             -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |
            |
            |
            --------""",
            """             -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  |
            |
            |
            --------""",
            """             -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | 
            |  | 
            |
            --------""",
            """             -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            |  | 
            |
            --------""",
            """             -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            |  | | 
            |   
            --------""")

        print(hangman[0])
        attempts = len(hangman) - 1

        while attempts != 0 and "-" in word_guessed:
            print("\nYou have {} attempts remaining".format(attempts))
            word_joined = "".join(word_guessed)
            print(word_joined)

            try:
                guessed_letter = str(input("\nEnter a letter between A-Z" + "\n> ")).lower()
            except:
                print("Not a valid input try again.")
                continue
            else:
                if not guessed_letter.isalpha():
                    print("Not a letter")
                    continue
                elif len(guessed_letter) > 1:
                    print("More than 1 letter at a time not allowed")
                    continue
                elif guessed_letter in letter_guessed:
                    print("Already guessed try with another")
                    continue
                else:
                    pass

            letter_guessed.append(guessed_letter)

            for letter in range(len(word_selected)):
                if guessed_letter == word_selected[letter]:
                    word_guessed[letter] = guessed_letter

            if guessed_letter not in word_selected:
                attempts -= 1
                print(hangman[(len(hangman) - 1) - attempts])

        if "-" not in word_guessed:
            print("\nYou Won got the word {}".format(word_selected))
        else:
            print("\nYou lose didn't got word {}.".format(word_selected))

        print("\nLike to Play Again? Y/N")

        choice = input("> ").lower()
        if choice not in ("yes", "y"):
            play_game = False


if __name__ == "__main__":
    main()
