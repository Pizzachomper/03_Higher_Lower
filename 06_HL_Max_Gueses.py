#Maximum gueses calculator
import math

#Loop component
for item in range(0, 4):

    low = int(input("Low: "))
    high = int(input("High: "))
    range = high - low + 1
    
    #Finds maximum number of guesses
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print(F"Max guesses: {max_guesses}")
    print()