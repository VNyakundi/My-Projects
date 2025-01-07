# This is a small project that shows managers details in the premier league
# This has a good illustration of Object Oriented Programming and the use of Inheritance to make the code more interesting

class League:
    def __init__(self,name,team,points):
        self.name = name
        self.team = team
        self.points = points

    def get_points(self):
        """get points of the team"""
        print(f"points:{self.points}")
        print(f"name:{self.name}")

class Manager:
    def __init__(self,manager_name,age,club_managed,trophies):
        self.manager_name = manager_name
        self.age = age
        self.club_managed = club_managed
        self.trophies = trophies

    def show_trophies(self):
        """show trophies won by the manager"""
        print(f"trophies:{self.trophies}")
        print(f"club managed:{self.club_managed}")
        print(f"age:{self.age}")
        print(f"manager name:{self.manager_name}")

class ManchesterUnited(League):
    def __init__(self,league_position,year_founded,number_of_trophies):
        self.league_position = league_position
        self.year_founded = year_founded
        self.number_of_trophies = number_of_trophies

    def show_team_stats(self):
        """show team statistics"""
        print("league position:{self.league_position}")
        print("year founded:{self.year_founded}")
        print("number of trophies:{self.number_of_trophies}")

    def manager(self):
        """show manager"""
        print(f"{self.name}manages a team{self.team}in the {self.league_position}")

if __name__ =="__main__":
    manager = Manager(manager_name="Ruben Amorim ",age = 45, club_managed = "Man United", trophies = 5)
    league = League(name = "Premier league",team = "Man United",points = 56)

    print("show trophies")
    manager.show_trophies()
    
    print("\nShow team stats")
    manager.show_trophies()

    print("\nShow League Stats")
    league.get_points()

