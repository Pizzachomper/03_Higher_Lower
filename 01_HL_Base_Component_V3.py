#Base component V3

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

def int_check(question, low=None, high=None, exit_code=None):
    
    #Check if user has entered a number between 1 - 100
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"
    
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        
        try:
            response =  int(response)
        
            # check that integer is valid (ie: not too low / too hig etc)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response
                    
            elif situation == "low only":
                if response >= low:
                    return response
            
            #Print out errors
            print(error)            
        
        except ValueError:
            print(error)
            
# main routine goes here

rounds_played = 0
rounds_won = 0
rounds_lost = 0
score = 0

low_number = 1
high_number = 100

guesses_allowed = 6

mode = "regular"

#Title
print()
print("*^* Welcome to Higher Lower *^*")
print()

#Ask user if they have played the game before
played_before = yes_no("Have you played this game before? ")
print(F"You choose {played_before}")
print()

if played_before == "no":
    instructions()

#Ask user how many rounds
rounds = int_check("How many rounds: ", 1, exit_code = "")
print()

if rounds == "":
    mode = "infinite"
    rounds = 5

#Rounds loop
end_game = "no"
while end_game == "no":

    secret = random.randint(1, 100)
    
    already_guessed = [] 

    # start of round (initialise already guessed list and reset guesses left)

    guesses_left = guesses_allowed
    
    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        
    print(heading)
    
    guess = ""
    # Start Round!!
    while guess != secret and guesses_left >= 1:
    
        #Ask user for their guess
        guess = int_check("What is your guess (1 - 100): ", low_number, high_number, "xxx")
        print("you guessed", guess)
        
        #check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You already guessed that number 😡! Please try again, You still have {guesses_left} guesses left.")
            print()
            continue

        already_guessed.append(guess)

        #Take away user guesses for each go
        guesses_left -= 1

        # Check user hasn't entered the same number again or exit code

        if guess == "xxx":
            end_game = "yes"
            break            
        
        #Compare guess to secret number
        #Too low or too high
        if guesses_left >= 1:
            
            if guess < secret:
                print(F"Too low, try a higher number. Guesses left {guesses_left}")
            elif guess > secret:
                print(F"Too high, try a lower number. Guesses left {guesses_left}")

            print()

        #Correctly guessed secret
        if guess == secret:
            
            rounds_played += 1
            rounds_won += 1
            print("You got it 🎊")
            print()
            score += 100
            score += guesses_left * 15
            break

        #User runs out of guesses
        if guesses_left <=0:
            print()
            if guess < secret:
                print("Too low!, GAME OVER 😭")

            elif guess > secret:
                print("Too high!, GAME OVER 😭")

            rounds_played += 1
            rounds_lost += 1
            print(F"Secret Number: {secret}")
            print()


    # check if we are out of rounds
    if rounds_played >= rounds:
        break
    
#Quick calculations
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

#End of game statements
print('***** End Game Summary  *****')
print(f"Wins: {rounds_won}, {percent_win:.0f}% \nLosses: {rounds_lost}, {percent_lose:.0f}%\nScore: {score} pts")
print()
print("Thanks for playing my game 😆")