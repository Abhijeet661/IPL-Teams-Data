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
dc = [
    Player(1,  "KL Rahul",           539,  0,  "DC"),   # Top run scorer 
    Player(12, "Abishek Porel",      301,  5,  "DC"),
    Player(21, "Tristan Stubbs",     300,  1,  "DC"),
    Player(32, "Ajay Mandal",        263,  5,  "DC"),
    Player(5,  "Vijay Nigam",        142, 11,  "DC"),
    Player(7,  "Kuldeep Yadav",       0, 15,  "DC"),
    Player(13, "Mukesh Kumar",        0, 12,  "DC"),
    Player(34, "Mohit Sharma",        0,  2,  "DC"),
    Player(11, "Mustafizur Rahman",   0,  4,  "DC"),
    Player(9,  "Dushmantha Chameera", 0,  4,  "DC"),
    Player(17, "Darshan Nalkande",    0,  0,  "DC"),
    Player(18, "Kulwant Khejroliya",  0,  0,  "DC"),
    Player(24, "Nitish Rana",        152,  1,  "DC"),   # Wicketkeeper / batsman
    Player(22, "Mitchell Marsh",     175,  0,  "DC"),
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
batsmen_above_500_runs(dc)
bowlers_above_20_wickets(dc)
players_with_r_in_name(dc)

print("\n 5th Position Team of IPL 2025: DC ")