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
mi = [
    Player(63, "Suryakumar Yadav", 717,   0, "MI"),
    Player(45, "Rohit Sharma",     418,   0, "MI"),
    Player(11, "Ryan Rickelton",   388,   0, "MI"),
    Player(9,  "Tilak Varma",      343,   0, "MI"),
    Player(13, "Naman Dhir",       252,   0, "MI"),
    Player(29, "Will Jacks",       233,   6, "MI"),
    Player(33, "Hardik Pandya",    224,  14, "MI"),
    Player(77, "Jonny Bairstow",    85,   0, "MI"),
    Player(7,  "Corbin Bosch",      47,   0, "MI"),
    Player(70, "Mitchell Santner",  40,  10, "MI"),
    Player(93, "Trent Boult",        1,  22, "MI"),
    Player(10, "Jasprit Bumrah",     0,  18, "MI"),
    Player(24, "Deepak Chahar",     28,  11, "MI"),
    Player(18, "Ashwani Kumar",      0,  11, "MI"),
    Player(41, "Karn Sharma",        0,   7, "MI"),
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
batsmen_above_500_runs(mi)
bowlers_above_20_wickets(mi)
players_with_r_in_name(mi)

print("\n 4th Position Team of IPL 2025: MI ")