#Number checking function goes here
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


#Guess number routine

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Round: ", 1)
guess = int_check("Guess: ", lowest, highest)