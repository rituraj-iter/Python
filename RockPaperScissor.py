import random
while True:
    player = input("Rock, Paper, Scissors ")
    computer = random.choice(['Rock', 'Paper', 'Scissors'])
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose")
        else:
            print("You win")
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose")
        else:
            print("You win")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose")
        else:
            print("You win")
    else:
        print("Check Word")
