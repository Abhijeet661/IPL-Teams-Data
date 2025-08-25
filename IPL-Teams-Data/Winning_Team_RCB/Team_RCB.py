''' Player has jn , name , runs ,wickets and team name. It has all get and set methods for every attribute. 
			Create team RCB with minimum 5 players in it(2025). 
			
			tasks:
				1. display all batsman from team RCB who scores more than 500 runs.
				2. Display all ballers from rcb who took more than 20 wickets .
				3. Display all players name whose name consist of "r" letter.
'''


# Player class
class Player:
    def __init__(self, jn, name, runs, wickets, team):
        self._jn = jn
        self._name = name
        self._runs = runs
        self._wickets = wickets
        self._team = team

    # Getters
    def get_jn(self): return self._jn
    def get_name(self): return self._name
    def get_runs(self): return self._runs
    def get_wickets(self): return self._wickets
    def get_team(self): return self._team

    # Setters
    def set_jn(self, jn): self._jn = jn
    def set_name(self, name): self._name = name
    def set_runs(self, runs): self._runs = runs
    def set_wickets(self, wickets): self._wickets = wickets
    def set_team(self, team): self._team = team
 

# TEAM CREATION (RCB Squad - 2025)
rcb = [
    Player(18, "Virat Kohli", 657, 0, "RCB"),
    Player(99, "Josh Hazlewood", 30, 22, "RCB"),
    Player(63, "Rajat Patidar", 312, 0, "RCB"),
    Player(61, "Phil Salt", 403, 0, "RCB"),
    Player(70, "Krunal Pandya", 109, 17, "RCB"),
    Player(93, "Bhuvneshwar Kumar", 14, 17, "RCB"),
    Player(10, "Jitesh Sharma", 261, 0, "RCB"),
    Player(7, "Tim David", 187, 0, "RCB"),
    Player(17, "Romario Shepherd", 70, 0, "RCB"),
    Player(57, "Yash Dayal", 4, 13, "RCB"),
    Player(44, "Anuj Rawat", 167, 0, "RCB")
]


# FUNCTIONS TO HANDLE TASKS
def batsmen_above_500_runs(team):
    print("1️. Batsmen from RCB with runs > 500:")
    found = False
    for player in team:
        if player.get_runs() > 500:
            print(f"   {player.get_name()} - {player.get_runs()} runs")
            found = True
    if not found:
        print("   No batsman scored above 500 runs.")

def bowlers_above_20_wickets(team):
    print("\n2️. Bowlers from RCB with wickets > 20:")
    found = False
    for player in team:
        if player.get_wickets() > 20:
            print(f"   {player.get_name()} - {player.get_wickets()} wickets")
            found = True
    if not found:
        print("   No bowler has more than 20 wickets.")

def players_with_r_in_name(team):
    print("\n3️. Players from RCB whose name contains letter 'r':")
    found = False
    for player in team:
        if "r" in player.get_name().lower():
            print(f"   {player.get_name()}")
            found = True
    if not found:
        print("   No player with the letter 'r' in their name.")


# MAIN PROGRAM EXECUTION
batsmen_above_500_runs(rcb)
bowlers_above_20_wickets(rcb)
players_with_r_in_name(rcb)

print("\n Winning Team of IPL 2025: RCB ")
