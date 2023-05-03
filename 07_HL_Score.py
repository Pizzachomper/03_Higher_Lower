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

 #Calculate Game Stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100


#End of game statements
print()
print('***** End Game Summary  *****')
print(f"Win: {rounds_won}, {percent_win:.0f}% \nLoss: {rounds_lost}, {percent_lose:.0f}%")
print()
print("Thanks for playing")