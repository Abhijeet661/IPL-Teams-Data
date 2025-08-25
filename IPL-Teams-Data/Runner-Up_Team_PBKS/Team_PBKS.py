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
pbks = [
    Player(96, "Shreyas Iyer",         603,  2, "PBKS"),   # Captain, Top scorer
    Player(84, "Prabhsimran Singh",    573,  0, "PBKS"),
    Player(18, "Priyansh Arya",        521,  0, "PBKS"),
    Player(19, "Nehal Wadhera",        354,  1, "PBKS"),
    Player(27, "Shashank Singh",       289,  4, "PBKS"),
    Player(2,  "Arshdeep Singh",        69, 23, "PBKS"),   # Leading wicket-taker
    Player(3,  "Yuzvendra Chahal",      18, 17, "PBKS"),
    Player(70, "Marco Jansen",          44, 15, "PBKS"),
    Player(17, "Marcus Stoinis",       276, 10, "PBKS"),
    Player(95, "Josh Inglis",          394,  0, "PBKS"),
    Player(13, "Harpreet Brar",         56, 12, "PBKS"),
    Player(9,  "Azmatullah Omarzai",    99, 11, "PBKS"),
    Player(15, "Xavier Bartlett",        8, 10, "PBKS"),
    Player(32, "Glenn Maxwell",         92,  6, "PBKS"),
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
batsmen_above_500_runs(pbks)
bowlers_above_20_wickets(pbks)
players_with_r_in_name(pbks)

print("\n Runner-Up Team of IPL 2025: PBKS ")
