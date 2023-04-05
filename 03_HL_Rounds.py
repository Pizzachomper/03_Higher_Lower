#Functions goes here
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