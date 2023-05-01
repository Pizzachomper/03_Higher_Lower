#scoring system

#Round won will be calculated
rounds_played = 0
rounds_won = 0
rounds_lost = 0

#Results for testing purposes
test_results = ["won", "won", "loss", "loss"]

#Play game
for item in test_results:
    rounds_played += 1

    #Generate computer choice

    result = item


    if result == "loss":
        result = "You lose"
        rounds_lost += 1


#Quick calculations
rounds_won = rounds_played - rounds_lost



#End of game statements
print()
print('***** End Game Summary  *****')
print(f"Won: {rounds_won} \t\t Lost: {rounds_lost}")
print()
print("Thanks for playing")