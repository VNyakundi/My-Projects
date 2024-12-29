# Create a program that shows team stats, player stats



league = {
    "Arsenal":{"points":0 ,"yellow cards":0,"penalties":0},
    "Manchester City":{"points":0 ,"yellow cards":0,"penalties":0},
    "Liverpool":{"points":0 ,"yellow cards":0,"penalties":0},
    "Manchester United":{"points":0 ,"yellow cards":0,"penalties":0},
    "Chelsea":{"points":0 ,"yellow cards":0,"penalties":0},
    "Tottenham":{"points":0 ,"yellow cards":0,"penalties":0},
    "Newcaste":{"points":0 ,"yellow cards":0,"penalties":0},
    "Aston Villa":{"points":0 ,"yellow cards":0,"penalties":0},

}

# list too store player stats
top_scorers = {}
top_assisters = {}

def display_table():
    """Display the current league table."""
    print("\nPremier league table:  ")
    sorted_teams = sorted(league.items(),key=lambda x:x[1]['points'],reverse = True)
    for i,(team,stats) in enumerate(sorted_teams,start = 1):
        print(f"{i}.{team}-points{stats['points']},yellow cards:{stats['yellow cards']},penalties{stats['penalties']}")

def update_points():
    """Update points after match week."""
    print("\nUpdate points")
    for team in league:
        try:
            points = int(input(f"enter points for team {team}: "))
            league[team]["points"] += points
        except ValueError:
            print("invalid input, please enter a number")

def record_yellow_cards():
    """Record yellow cards for each team."""
    print("\nRecord Yellow Cards:")
    for team in league:
        try:
            yellow_cards = int(input(f"Enter yellow cards for {team}: "))
            league[team]["yellow_cards"] += yellow_cards
        except ValueError:
            print("Invalid input. Please enter a number.")

def record_penalties():
    """Record number of penalties awarded in every match week"""
    print("\nRecord penalties: ")
    for team in league:
        try:
            penalties = int(input("Enter number of penalties awareded to {team}: "))
            league[team]["penalties"]+=penalties
        except ValueError:
            print("invalid input, please enter a number")

def update_player_stats():
    """Update top scorers and top assister"""
    print("\nUpdate player stats")
    try:
        scorer = input("Enter the name of the top scorer this week: ")
        goals = int(input(f"Enter the number of goals by {scorer}:"))
        top_scorers[scorer] = top_scorers.get(scorer,0)+goals

        assister = input("Enter the name of the top assister this week: ")
        assists = int(input(f"Enter the number of assists by {assister}:"))
        top_assisters[assister] = top_assisters.get(assister,0)+assists

    except ValueError:
        print("invalid input,please try again")

def display_player_stats():
    """Display top scorers and assisters"""
    print("\nTop Scorers: ")
    for player, goals in sorted(top_scorers.items(),key = lambda x:x[1],reverse=True):
         print(f"{player} - {goals} goals")

    print("\nTop Assisters: ")
    for player, assists in sorted(top_assisters.items(),key = lambda x:x[1],reverse=True):
         print(f"{player} - {assists} assists")

def main():
    """Main function to run the program."""
    while True:
        print("\nOptions: ")
        print("1. View League table")
        print("2. Update points")
        print("3. Record yellow cards")
        print("4. Record penalties")
        print("5. Update player stats")
        print("6. View player stats")
        print("7. Exit")

        choice = input("choose an option")
        if choice == "1":
            display_table()
        elif choice == "2":
            update_points()
        elif choice == "3":
            record_yellow_cards()
        elif choice == "4":
            record_penalties()
        elif choice == "5":
            update_player_stats()
        elif choice == "6":
            display_player_stats()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("invalid choice, please try again")

if __name__ == "__main__":
    main()
