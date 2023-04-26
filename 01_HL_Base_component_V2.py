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
You have only 9 attempts to guess the number. But if you dont want to play anymore type xxx or x to quit, 
you can see your game summary at the end of your game and how many guesses you have done. 
Enjoy 😆
    
    ''')

    return ""

def check_rounds():
    
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                #If infinite mode not chosen, check response
                response = int(response)

                #Start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue


        return response

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
secret = 7
guesses_allowed = 5

already_guessed = [] 
guesses_left = guesses_allowed
num_won = 0

guess = ""

rounds_played = 0


rounds = check_rounds()
end_game = "no"

while end_game == "no":

    #Start of GamePlay Loop

    #Rounds heading
    print()
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
    
    print(heading)

    #End game if exit code is typed
    if guess == "xxx":
        break

    #Rest of loop / game
    print(f"You choose {guess}")

    rounds_played += 1
    #end_game if requested number of rounds have been played
    if rounds_played == rounds:
        break

#Havn't guessed number
while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))

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
    
    else:
        if guess < secret:
            print("Too low!, GAME OVER 😭")
        elif guess > secret:
            print("Too high!, GAME OVER 😭")

#Correctly guessed number
if guess == secret:
    if guesses_left == guesses_allowed:
        print("Amazing you got it 😣")
    else:
        print("You got it 🎊")


#Put endgame content here
print()
print("Thank you for playing my game 😆")