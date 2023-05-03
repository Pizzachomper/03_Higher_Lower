import random
import math
#Functions go here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

def instructions():

    print('''
^*^ How to Play Higher Lower ^*^
This is a game made to play Higher/Lower in python. 
Answer with how many rounds you will play or type enter for infinite mode. 
Please type a number between 1-100 and see if you can find the computer choice.
The computer will respond if the number is higher or lower than the given response.
You have only 6 attempts to guess the number. But if you dont want to play anymore type xxx to quit, 
you can see your game summary at the end of your game and how many guesses you have done. 
Enjoy 😆
    
    ''')

    return ""

def int_check(question, low=None, high=None):

    situation = ""


    #Check if low and high number are correct
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        
        try:
            response = int(input(question))

            #Check if response is too high or too low
            if situation == "both":
                if response < low or response > high:
                    print(F"Please enter a number between {low} and {high}")

            #Check response is not too low
            elif situation == "low only":
                if response < low:
                    print(F"Please enter a number that is more than or equal to {low}")
                    continue

            else:
                print("please answer yes / no")
            
            return response
        
        #check input is a integer
        except ValueError:
            print("Please enter an integer")
            continue


#Ask user if they have played before
#If yes, show instructions

played_before = yes_no("Have you played this game before? ")
print(F"You choose {played_before}")

if played_before == "no":
    instructions()

#Ask user for # of rounds, enter for INFINITE MODE
#Rounds routine goes here

#Prevent duplicate guesses
#Generate secret number between 1 to 100
secret = random.randint(1, 100)

guesses_allowed = 6

already_guessed = [] 
guesses_left = guesses_allowed
num_won = 0

guess = ""

rounds_played = 0
rounds_lost = 0
rounds_won = 0


#Havn't guessed number
while guess != secret and guesses_left >= 1:

    guess = int_check("What is your guess?: ", 1, 100)

    #check that guess is not a duplicate
    if guess in already_guessed:
        print(F"You already guessed that number 😡! Please try again, You still have {guesses_left} guesses left.")
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    #Too low or too high
    if guesses_left >= 1:
        
        if guess < secret:
            print(F"Too low, try a higher number. Guesses left {guesses_left}")
        elif guess > secret:
            print(F"Too high, try a lower number. Guesses left {guesses_left}")
    

    elif guess == "xxx":
        break

    #Game over
    else:
        if guess < secret:
            print("Too low!, GAME OVER 😭")
            print(F"Secret: {secret}")
            result = "loss"
        elif guess > secret:
            print("Too high!, GAME OVER 😭")
            print(F"Secret: {secret}")
            result = "loss"


#Correctly guessed number
if guess == secret:
    if guesses_left == guesses_allowed:
        print("Amazing you got it 😣")
        result = "win"
    else:
        print("You got it 🎊")
        result = "win"


#Put endgame content here
if result == "loss":
    rounds_lost += 1
    rounds_played += 1

if result == "win":
    rounds_won += 1
    rounds_played += 1

yes_no("Do you want to play again?: ")

#Quick calculations

percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

#End of game statements
print()
print('***** End Game Summary  *****')
print(f"Win: {rounds_won}, {percent_win:.0f}% \nLoss: {rounds_lost}, {percent_lose:.0f}%")
print()
print("Thanks for playing my game 😆")