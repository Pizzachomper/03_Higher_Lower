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

#Ask user if they have played before
#If yes, show instructions

played_before = yes_no("Have you played this game before? ")
print(F"You choose {played_before}")

if played_before == "no":
    instructions()
