# MAIN CONFIG
# -------------------------------------------------------------------------------------------------------
year = 2014
is_finished = True

is_roster_scraped = True
is_player_scraped = True
is_team_scraped = True
is_season_scraped = True

# TODO: aprimorar a estrutura do dicionário para reutilização
# Lista de Times
teams = {
    'buf': 'BUF', 'mia': 'MIA', 'nwe': 'NWE', 'nyj': 'NYJ',
    'pit': 'PIT', 'rav': 'BAL', 'cin': 'CIN', 'cle': 'CLE',
    'htx': 'HOU', 'clt': 'IND', 'oti': 'TEN', 'jax': 'JAX', 
    'kan': 'KAN', 'sdg': 'SDG', 'den': 'DEN', 'rai': 'RAI',
    'phi': 'PHI', 'was': 'WAS', 'dal': 'DAL', 'nyg': 'NYG',
    'det': 'DET', 'min': 'MIN', 'gnb': 'GNB', 'chi': 'CHI',
    'atl': 'ATL', 'tam': 'TAM', 'nor': 'NOR', 'car': 'CAR',
    'crd': 'ARI', 'ram': 'RAM', 'sea': 'SEA', 'sfo': 'SFO'
}

#TODO: Melhorar isto
# TEAMS TO CSV
# -------------------------------------------------------------------------------------------------------
teams_csv = [
    ['Tm','Name','Conference','Division'],
    ['ARI','Arizona Cardinals','NFC','West'],
    ['ATL','Atlanta Falcons','NFC','South'],
    ['BAL','Baltimore Ravens','AFC','North'],
    ['BUF','Buffalo Bills','AFC','East'],
    ['CAR','Carolina Panthers','NFC','South'],
    ['CHI','Chicago Bears','NFC','North'],
    ['CIN','Cincinnati Bengals','AFC','North'],
    ['CLE','Cleveland Browns','AFC','North'],
    ['DAL','Dallas Cowboys','NFC','East'],
    ['DEN','Denver Broncos','AFC','West'],
    ['DET','Detroit Lions','NFC','North'],
    ['GNB','Green Bay Packers','NFC','North'],
    ['HOU','Houston Texans','AFC','South'],
    ['IND','Indianapolis Colts','AFC','South'],
    ['JAX','Jacksonville Jaguars','AFC','South'],
    ['KAN','Kansas City Chiefs','AFC','West'],
    ['RAI','Las Vegas Raiders','AFC','West'],
    ['SDG','Los Angeles Chargers','AFC','West'],
    ['RAM','Los Angeles Rams','NFC','West'],
    ['MIA','Miami Dolphins','AFC','East'],
    ['MIN','Minnesota Vikings','NFC','North'],
    ['NWE','New England Patriots','AFC','East'],
    ['NOR','New Orleans Saints','NFC','South'],
    ['NYG','New York Giants','NFC','East'],
    ['NYJ','New York Jets','AFC','East'],
    ['PHI','Philadelphia Eagles','NFC','East'],
    ['PIT','Pittsburgh Steelers','AFC','North'],
    ['SFO','San Francisco 49ers','NFC','West'],
    ['SEA','Seattle Seahawks','NFC','West'],
    ['TAM','Tampa Bay Buccaneers','NFC','South'],
    ['TEN','Tennessee Titans','AFC','South'],
    ['WAS','Washington Commanders','NFC','East']
]

# FOLDERS
# -------------------------------------------------------------------------------------------------------
AWARDS = "data/raw/awards"
ROSTERS = "data/raw/rosters"
COACHES = "data/raw/coaches"
DRAFT = "data/raw/draft"
SCHEDULE = "data/raw/schedule"

# Normal
STATS_PLAYER = "data/raw/stats/player"
STATS_TEAM = "data/raw/stats/team/"

# Advanced
STATS_ADV_PLAYER = f"data/raw/Stats/player/advanced"
STATS_ADV_TEAM = f"data/raw/Stats/team/advanced"

# list of folders
folders = [
    AWARDS,
    ROSTERS,
    COACHES,
    DRAFT,
    SCHEDULE,
    STATS_TEAM,
    STATS_PLAYER,
    STATS_ADV_PLAYER,
    STATS_ADV_TEAM,
]

# FILES
# -------------------------------------------------------------------------------------------------------
AP = "AP.csv"
PB = "PB.csv"

# Coaches
coaches = "coaches.csv"

# Draft
draft = "draft.csv"

# Rosters
rosters = "rosters.csv"

# Schedule
games = "games.csv"

# Player Stats (Advanced)
player_adv_passing = "player_adv_passing.csv"
player_adv_rushing = "player_adv_rushing.csv"
player_adv_receiving = "player_adv_receiving.csv"
player_adv_defense = "player_adv_defense.csv"

# Player Stats
player_defense = "player_defense.csv"
player_kicking = "player_kicking.csv"
player_passing = "player_passing.csv"
player_punting = "player_punting.csv"
player_receiving = "player_receiving.csv"
player_returns = "player_returns.csv"
player_rushing = "player_rushing.csv"

# Team Stats (Advanced)
team_adv_accuracy = "team_adv_accuracy.csv"
team_adv_air_yards = "team_adv_air_yards.csv"
team_adv_play_type = "team_adv_play_type.csv"
team_adv_pressure = "team_adv_pressure.csv"
team_adv_rushing = "team_adv_rushing.csv"
team_adv_receiving = "team_adv_receiving.csv"
team_adv_defense = "team_adv_defense.csv"

# Team Stats (Offense)
off_drives = "off_drives.csv"
off_kicking = "off_kicking.csv"
off_passing = "off_passing.csv"
off_punting = "off_punting.csv"
off_returns = "off_returns.csv"
off_rushing = "off_rushing.csv"
off_team_conversions = "off_team_conversions.csv"
off_team_scoring = "off_team_scoring.csv"
off_team_stats = "off_team_stats.csv"

# Team Stats (Defense)
def_drives = "def_drives.csv"
def_kicking = "def_kicking.csv"
def_passing = "def_passing.csv"
def_punting = "def_punting.csv"
def_returns = "def_returns.csv"
def_rushing = "def_rushing.csv"
def_team_conversions = "def_team_conversions.csv"
def_team_scoring = "def_team_scoring.csv"
def_team_stats = "def_team_stats.csv"

# TEAM SAVE DICT
# ------------------------------------------------------------------------------------------------
team_off_save_dict = {
    # Offense
    'team_stats': off_team_stats,
    'passing': off_passing,
    'rushing': off_rushing,
    'returns': off_returns,
    'kicking': off_kicking,
    'team_scoring': off_team_scoring,
    'team_conversions': off_team_conversions,
    'punting': off_punting,
    'drives': off_drives,
}

team_def_save_dict = {
    # Defense
    'team_stats': def_team_stats,
    'passing': def_passing,
    'rushing': def_rushing,
    'returns': def_returns,
    'kicking': def_kicking,
    'team_scoring': def_team_scoring,
    'team_conversions': def_team_conversions,
    'punting': def_punting,
    'drives': def_drives
}

# FILES TO MOVE
# ------------------------------------------------------------------------------------------------
FILES_TO_MOVE = {
    # Awards
    AP : f"{AWARDS}/AP/{year}.csv",
    PB: f"{AWARDS}/PB/{year}.csv",

    # Coaches
    coaches : f"{COACHES}/{year}.csv",

    # Draft
    draft : f"{DRAFT}/{year}.csv",

    # Rosters
    rosters : f"{ROSTERS}/{year}.csv",

    # Schedule
    games : f"{SCHEDULE}/{year}.csv",

    # Player Stats (Advanced)
    player_adv_passing : f"{STATS_PLAYER}/advanced/passing/{year}.csv",
    player_adv_rushing : f"{STATS_PLAYER}/advanced/rushing/{year}.csv",
    player_adv_receiving : f"{STATS_PLAYER}/advanced/receiving/{year}.csv",
    player_adv_defense : f"{STATS_PLAYER}/advanced/defense/{year}.csv",

    # Player Stats
    player_defense : f"{STATS_PLAYER}/defense/{year}.csv",
    player_kicking : f"{STATS_PLAYER}/kicking/{year}.csv",
    player_passing : f"{STATS_PLAYER}/passing/{year}.csv",
    player_punting : f"{STATS_PLAYER}/punting/{year}.csv",
    player_receiving : f"{STATS_PLAYER}/receiving/{year}.csv",
    player_returns : f"{STATS_PLAYER}/returns/{year}.csv",
    player_rushing : f"{STATS_PLAYER}/rushing/{year}.csv",

    # Team Stats (Advanced)
    team_adv_accuracy : f"{STATS_TEAM}/advanced/passing/accuracy/{year}.csv",
    team_adv_air_yards : f"{STATS_TEAM}/advanced/passing/air yards/{year}.csv",
    team_adv_play_type : f"{STATS_TEAM}/advanced/passing/play type/{year}.csv",
    team_adv_pressure : f"{STATS_TEAM}/advanced/passing/pressure/{year}.csv",
    team_adv_rushing : f"{STATS_TEAM}/advanced/rushing/{year}.csv",
    team_adv_receiving : f"{STATS_TEAM}/advanced/receiving/{year}.csv",
    team_adv_defense : f"{STATS_TEAM}/advanced/defense/{year}.csv",

    # Team Stats (Offense)
    off_drives : f"{STATS_TEAM}/offense/drives/{year}.csv",
    off_kicking : f"{STATS_TEAM}/offense/kicking/{year}.csv",
    off_passing : f"{STATS_TEAM}/offense/passing/{year}.csv",
    off_punting : f"{STATS_TEAM}/offense/punting/{year}.csv",
    off_returns : f"{STATS_TEAM}/offense/returns/{year}.csv",
    off_rushing : f"{STATS_TEAM}/offense/rushing/{year}.csv",
    off_team_conversions : f"{STATS_TEAM}/offense/team_conversions/{year}.csv",
    off_team_scoring : f"{STATS_TEAM}/offense/team_scoring/{year}.csv",
    off_team_stats : f"{STATS_TEAM}/offense/team_stats/{year}.csv",

    # Team Stats (Defense)
    def_drives : f"{STATS_TEAM}/defense/drives/{year}.csv",
    def_kicking : f"{STATS_TEAM}/defense/kicking/{year}.csv",
    def_passing : f"{STATS_TEAM}/defense/passing/{year}.csv",
    def_punting : f"{STATS_TEAM}/defense/punting/{year}.csv",
    def_returns : f"{STATS_TEAM}/defense/returns/{year}.csv",
    def_rushing : f"{STATS_TEAM}/defense/rushing/{year}.csv",
    def_team_conversions : f"{STATS_TEAM}/defense/team_conversions/{year}.csv",
    def_team_scoring : f"{STATS_TEAM}/defense/team_scoring/{year}.csv",
    def_team_stats : f"{STATS_TEAM}/defense/team_stats/{year}.csv"
}