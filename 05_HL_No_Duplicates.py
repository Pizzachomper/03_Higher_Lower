#Prevent duplicate guesses
secret = 7
guesses_allowed = 5

already_guessed = [] 
guesses_left = guesses_allowed
num_won = 0

guess = ""

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

