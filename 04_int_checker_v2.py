def int_check(question, low=None, high=None, exit_code=None):
    
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
            
            print(error)            
        
        except ValueError:
            print(error)
            
# main routine goes here

rounds_played = 0
rounds_won = 0

low_number = 1
high_number = 10

mode = "regular"

rounds = int_check("How many rounds: ", 1, exit_code = "")

if rounds == "":
    mode = "infinite"
    rounds = 5

# rounds loop
end_game = "no"
while end_game == "no":
    
    if mode == "infinite":
        heading = f"Round {rounds_played + 1} continues mode"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        
    print(heading)
        
    rounds_played += 1
        
    # Start Round!!
    while True:
        
        secret = 7
  
        guess = int_check("What is your Guess: ", low_number, high_number, "xxx")
        print("you guessed", guess)   
        
        if guess == "xxx":
            end_game = "yes"
            break    

        if guess == secret:
            rounds_won += 1
            break
        
    # check if we are out of rounds
    if rounds_played >= rounds:
        break
    
    