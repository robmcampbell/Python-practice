import random
import time

value=random.randint(1,100)

#Introduction
print("Hello! In Campbell production's latest game, I have randomly picked a number between 1 and 100. You need to guess the number in less than 6 guesses to win!")
time.sleep(3)

#Guessing loop
count = 0
while(count<6):
    count += 1
    rounds_left = 6 - count
    guess=input("Round " + str(count) + ": Make your guess! ")
    if(False==guess.isdigit() or float(guess)>=101):
        print("Try again! Make sure you write a digit between 1 and 100.")
        count -= 1
        time.sleep(1)
    elif(True==guess.isdigit()):
        guess = int(guess)
        if((guess>value) and (count<6)):
            print("Too big, try again. " + str(rounds_left) + " guesses left!")
        if((guess<value) and (count<6)):
            print("Too small, try again. " + str(rounds_left) + " guesses left!")
        if(guess==value):
            count += 10
        time.sleep(1)

        
#Final outcome
if(guess==value):
    print("Congratulations, you've won the game!")
else:
    print("You didn't win this time, the correct number was", value, "good luck on the next go!")
