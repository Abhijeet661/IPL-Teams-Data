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
gt = [
    Player(1,  "Sai Sudharsan",      759, 0,   "GT"),
    Player(3,  "Shubman Gill",       650, 0,   "GT"),
    Player(7,  "Jos Buttler",        538, 0,   "GT"),
    Player(23, "Sherfane Rutherford",291, 0,   "GT"),
    Player(51, "Shahrukh Khan",      179, 5,   "GT"),
    Player(16, "Rahul Tewatia",       99, 2,   "GT"),
    Player(50, "Mahipal Lomror",      92, 4,   "GT"),
    Player(19, "Rashid Khan",         40, 9,   "GT"),
    Player(27, "Washington Sundar",  133, 2,   "GT"),
    Player(12, "Prasidh Krishna",     13, 25,  "GT"),
    Player(11, "Mohammed Siraj",      3, 16,   "GT"),
    Player(80, "Kagiso Rabada",       9, 2,    "GT"),
    Player(24, "R Sai Kishore",       5, 19,   "GT"),
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
batsmen_above_500_runs(gt)
bowlers_above_20_wickets(gt)
players_with_r_in_name(gt)

print("\n 3rd Position Team of IPL 2025: GT ")
