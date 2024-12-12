import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)


    return roll

while True:
    players = input("enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            break
        else:
            print("must be between 2-4 players")
    else:
        print("invalid try again")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score)<max_score:
    for player_idx in range(players):
        print("\n player number",player_idx+1,"turn has just started")
        print("your total score is:",players_score[player_idx],"\n")
        current_score = 0


        while True:
             should_roll = input("would you want to roll (y)? ")
             if should_roll != "y":
                 break

             value = roll()
             if value == 1:
                  print("you rolled a 1! turn done!")
                  current_score = 0
                  break
             else:
                 current_score += value
                 print("you rolled a:", value)

             print("your score is:", current_score)
        players_score[player_idx] += current_score 
print("your total score is: ",players_score[player_idx])

max_score = max(players_score)
winning_idx = players_score.index(max_score)

print("player number", winning_idx + 1, "is the winner with a score of:", max_score)