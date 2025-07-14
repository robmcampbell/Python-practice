import time
import random

#Setting varibles up
compwin = 0
userwin = 0
OPTIONS = ("Rock", "Paper", "Scissors")

#Introducing the game
print("Welcome to rock, paper, scissors. You'll play against the computer to best of three. Here we go...")
print()
time.sleep(2)

#Body of game
while (compwin + userwin<3):
    choice = input("Do you want to play: \nRock \nPaper \nScissors \n").capitalize()
    if choice not in OPTIONS:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.\n")
        time.sleep(1)
        continue  # Don't count this round
    print()
    print("The computer chooses...")
    time.sleep(1)
    computer_choice = random.choice(OPTIONS)
    print(computer_choice)
    print()
    time.sleep(1)
    if((computer_choice == "Rock" and choice == "Rock") or (computer_choice == "Scissors" and choice == "Scissors") or (computer_choice == "Paper" and choice == "Paper")):
            print("It's a draw, try again!")
    if((computer_choice == "Rock" and choice == "Scissors") or (computer_choice == "Scissors" and choice == "Paper") or (computer_choice == "Paper" and choice == "Rock")):
            print("Computer wins this round!")
            compwin += 1
    if((computer_choice == "Rock" and choice == "Paper") or (computer_choice == "Scissors" and choice == "Rock") or (computer_choice == "Paper" and choice == "Scissors")):
            print("Well done, you win this round!")
            userwin += 1
    print()
    time.sleep(2)
    
#Announcing the results
if (compwin >= userwin):
    winner = "The computer!"
    number_of_wins = compwin
if (userwin >= compwin):
    winner = "You!"
    number_of_wins = userwin
print("And the winner... with", number_of_wins, "wins, is...")
time.sleep(2)
print(winner)
time.sleep(1)
if winner == "the computer":
    print("Better luck next time! Goodbye")
else:
    print("Congratulations, and thank you for playing!")
