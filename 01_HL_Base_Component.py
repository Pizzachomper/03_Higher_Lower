import random
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

#Ask user if they have played before
#If yes, show instructions

played_before = yes_no("Have you played this game before? ")
print(F"You choose {played_before}")

if played_before == "no":
    instructions()

#Ask user for # of rounds, enter for INFINITE MODE

#Main routine goes here

rounds_played = 0
choose_instruction = "Please enter a number that is between 1 and 100"


rounds = check_rounds()
end_game = "no"

while end_game == "no":

    #Start of game Play Loop

    #Rounds heading
    print()
    if rounds == "":
        heading = f"Continous Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
    
    print(heading)
    choose = input(f"{choose_instruction} or 'xxx' to end: ")

    #End game if exit code is typed
    if choose == "xxx":
        break

    #Rest of loop / game
    print(f"You choose {choose}")

    rounds_played += 1
    #end_game if requested number of rounds have been played
    if rounds_played == rounds:
        break

#Put endgame content here
print()
print("Thank you for playing my game 😆")