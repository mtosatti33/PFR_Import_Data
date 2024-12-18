# MAIN CONFIG
# -------------------------------------------------------------------------------------------------------
is_finished = True

# Enable downloads
is_roster_scraped = False
is_gamelogs_scraped = True
is_gamelogs_opp_scraped = True
is_player_scraped = False
is_team_scraped = False
is_season_scraped = False
is_images_downloaded = False

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

# TEAMS TO CSV
# -------------------------------------------------------------------------------------------------------
teams_csv = [
    ["Tm","Team","City","State","Conference","Division","Lat","Long","Logo"],
    ["ARI","Arizona Cardinals","Glendale"," Arizona","NFC","West","33,50805556","-112,2877778","img/logos/ARI.png"],
    ["ATL","Atlanta Falcons","Atlanta"," Georgia","NFC","South","33,75444444","-84,39055556","img/logos/ATL.png"],
    ["BAL","Baltimore Ravens","Baltimore"," Maryland","AFC","North","39,28861111","-76,62222222","img/logos/BAL.png"],
    ["BUF","Buffalo Bills","Orchard Park"," New York","AFC","East","42,92194444","-78,74222222","img/logos/BUF.png"],
    ["CAR","Carolina Panthers","Charlotte"," North Carolina","NFC","South","35,22944444","-80,90611111","img/logos/CAR.png"],
    ["CHI","Chicago Bears","Chicago"," Illinois","NFC","North","41,8825","-87,63916667","img/logos/CHI.png"],
    ["CIN","Cincinnati Bengals","Cincinnati"," Ohio","AFC","North","39,16083333","-84,5175","img/logos/CIN.png"],
    ["CLE","Cleveland Browns","Cleveland"," Ohio","AFC","North","41,50416667","-81,68138889","img/logos/CLE.png"],
    ["DAL","Dallas Cowboys","Arlington"," Texas","NFC","East","32,73805556","-97,12416667","img/logos/DAL.png"],
    ["DEN","Denver Broncos","Denver"," Colorado","AFC","West","39,75916667","-104,9811111","img/logos/DEN.png"],
    ["DET","Detroit Lions","Detroit"," Michigan","NFC","North","42,39055556","-83,08166667","img/logos/DET.png"],
    ["GNB","Green Bay Packers","Green Bay"," Wisconsin","NFC","North","44,86111111","-88,03055556","img/logos/GNB.png"],
    ["HOU","Houston Texans","Houston"," Texas","AFC","South","29,76333333","-95,37055556","img/logos/HOU.png"],
    ["IND","Indianapolis Colts","Indianapolis"," Indiana","AFC","South","39,96416667","-86,17666667","img/logos/IND.png"],
    ["JAX","Jacksonville Jaguars","Jacksonville"," Florida","AFC","South","30,32222222","-81,62861111","img/logos/JAX.png"],
    ["KAN","Kansas City Chiefs","Kansas City"," Missouri","AFC","West","39,16194444","-94,58777778","img/logos/KAN.png"],
    ["RAI","Las Vegas Raiders","Paradise"," Nevada","AFC","West","36,1425","-115,3163889","img/logos/RAI.png"],
    ["SDG","Los Angeles Chargers","Inglewood"," California","AFC","West","33,93","-118,3641667","img/logos/SDG.png"],
    ["RAM","Los Angeles Rams","Inglewood"," California","NFC","West","33,93","-118,3641667","img/logos/RAM.png"],
    ["MIA","Miami Dolphins","Miami Gardens"," Florida","AFC","East","25,97555556","-80,22138889","img/logos/MIA.png"],
    ["MIN","Minnesota Vikings","Minneapolis"," Minnesota","NFC","North","44,97972222","-93,25555556","img/logos/MIN.png"],
    ["NWE","New England Patriots","Foxborough"," Massachusetts","AFC","East","42,11694444","-71,21583333","img/logos/MWE.png"],
    ["NOR","New Orleans Saints","New Orleans"," Louisiana","NFC","South","29,95138889","-90,07","img/logos/NOR.png"],
    ["NYG","New York Giants","East Rutherford"," New Jersey","NFC","East","40,84083333","-74,13833333","img/logos/NYG.png"],
    ["NYJ","New York Jets","East Rutherford"," New Jersey","AFC","East","40,84083333","-74,13833333","img/logos/NYJ.png"],
    ["PHI","Philadelphia Eagles","Philadelphia"," Pennsylvania","NFC","East","40","-75,21666667","img/logos/PHI.png"],
    ["PIT","Pittsburgh Steelers","Pittsburgh"," Pennsylvania","AFC","North","40,4375","-79,97861111","img/logos/PIT.png"],
    ["SFO","San Francisco 49ers","Santa Clara"," California","NFC","West","37,4125","-121,9055556","img/logos/SFO.png"],
    ["SEA","Seattle Seahawks","Seattle"," Washington","NFC","West","47,60305556","-122,3475","img/logos/SEA.png"],
    ["TAM","Tampa Bay Buccaneers","Tampa"," Florida","NFC","South","27,93666667","-82,595","img/logos/TAM.png"],
    ["TEN","Tennessee Titans","Nashville"," Tennessee","AFC","South","36,16611111","-86,80444444","img/logos/TEN.png"],
    ["WAS","Washington Commanders","Landover"," Maryland","NFC","East","38,94555556","-76,94833333","img/logos/WAS.png"]
]

# FOLDERS
# -------------------------------------------------------------------------------------------------------
AWARDS = "data/raw/awards"
ROSTERS = "data/raw/rosters"
COACHES = "data/raw/coaches"
DRAFT = "data/raw/draft"
SCHEDULE = "data/raw/schedule"
GAMELOGS = "data/raw/gamelogs"

# Normal
STATS_PLAYER = "data/raw/stats/player"
STATS_TEAM = "data/raw/stats/team/"

# Advanced
STATS_ADV_PLAYER = f"data/raw/Stats/player/advanced"
STATS_ADV_TEAM = f"data/raw/Stats/team/advanced"

# Team Logos
TEAM_LOGOS = "img/logos/"

# list of folders
folders = [
    AWARDS,
    ROSTERS,
    COACHES,
    DRAFT,
    SCHEDULE,
    GAMELOGS,
    STATS_TEAM,
    STATS_PLAYER,
    STATS_ADV_PLAYER,
    STATS_ADV_TEAM
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

# Gamelogs
gamelogs = "gamelogs.csv"
gamelogs_opp = "gamelogs_opp.csv"

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
    AP : f"{AWARDS}/AP/" + "{}.csv",
    PB: f"{AWARDS}/PB/" + "{}.csv",

    # Coaches
    coaches : f"{COACHES}/" + "{}.csv",

    # Draft
    draft : f"{DRAFT}/" + "{}.csv",

    # Rosters
    rosters : f"{ROSTERS}/" + "{}.csv",

    # Gamelogs
    gamelogs : f"{GAMELOGS}/team/" + "{}.csv",
    gamelogs_opp: f"{GAMELOGS}/opp/" + "{}.csv",

    # Schedule
    games : f"{SCHEDULE}/" + "{}.csv",

    # Player Stats (Advanced)
    player_adv_passing : f"{STATS_PLAYER}/advanced/passing/" + "{}.csv",
    player_adv_rushing : f"{STATS_PLAYER}/advanced/rushing/" + "{}.csv",
    player_adv_receiving : f"{STATS_PLAYER}/advanced/receiving/" + "{}.csv",
    player_adv_defense : f"{STATS_PLAYER}/advanced/defense/" + "{}.csv",

    # Player Stats
    player_defense : f"{STATS_PLAYER}/defense/" + "{}.csv",
    player_kicking : f"{STATS_PLAYER}/kicking/" + "{}.csv",
    player_passing : f"{STATS_PLAYER}/passing/" + "{}.csv",
    player_punting : f"{STATS_PLAYER}/punting/" + "{}.csv",
    player_receiving : f"{STATS_PLAYER}/receiving/" + "{}.csv",
    player_returns : f"{STATS_PLAYER}/returns/" + "{}.csv",
    player_rushing : f"{STATS_PLAYER}/rushing/" + "{}.csv",

    # Team Stats (Advanced)
    team_adv_accuracy : f"{STATS_TEAM}/advanced/passing/accuracy/" + "{}.csv",
    team_adv_air_yards : f"{STATS_TEAM}/advanced/passing/air yards/" + "{}.csv",
    team_adv_play_type : f"{STATS_TEAM}/advanced/passing/play type/" + "{}.csv",
    team_adv_pressure : f"{STATS_TEAM}/advanced/passing/pressure/" + "{}.csv",
    team_adv_rushing : f"{STATS_TEAM}/advanced/rushing/" + "{}.csv",
    team_adv_receiving : f"{STATS_TEAM}/advanced/receiving/" + "{}.csv",
    team_adv_defense : f"{STATS_TEAM}/advanced/defense/" + "{}.csv",

    # Team Stats (Offense)
    off_drives : f"{STATS_TEAM}/offense/drives/" + "{}.csv",
    off_kicking : f"{STATS_TEAM}/offense/kicking/" + "{}.csv",
    off_passing : f"{STATS_TEAM}/offense/passing/" + "{}.csv",
    off_punting : f"{STATS_TEAM}/offense/punting/" + "{}.csv",
    off_returns : f"{STATS_TEAM}/offense/returns/" + "{}.csv",
    off_rushing : f"{STATS_TEAM}/offense/rushing/" + "{}.csv",
    off_team_conversions : f"{STATS_TEAM}/offense/team_conversions/" + "{}.csv",
    off_team_scoring : f"{STATS_TEAM}/offense/team_scoring/" + "{}.csv",
    off_team_stats : f"{STATS_TEAM}/offense/team_stats/" + "{}.csv",

    # Team Stats (Defense)
    def_drives : f"{STATS_TEAM}/defense/drives/" + "{}.csv",
    def_kicking : f"{STATS_TEAM}/defense/kicking/" + "{}.csv",
    def_passing : f"{STATS_TEAM}/defense/passing/" + "{}.csv",
    def_punting : f"{STATS_TEAM}/defense/punting/" + "{}.csv",
    def_returns : f"{STATS_TEAM}/defense/returns/" + "{}.csv",
    def_rushing : f"{STATS_TEAM}/defense/rushing/" + "{}.csv",
    def_team_conversions : f"{STATS_TEAM}/defense/team_conversions/" + "{}.csv",
    def_team_scoring : f"{STATS_TEAM}/defense/team_scoring/" + "{}.csv",
    def_team_stats : f"{STATS_TEAM}/defense/team_stats/" + "{}.csv"
}

# -------------------------------------------------------------------------------------------------------
teams_regex = {
    r'New Orleans Saints': 'NOR',
    r'Jacksonville Jaguars': 'JAX',
    r'Houston Texans': 'HOU',
    r'New England Patriots': 'NWE',
    r'Cleveland Browns': 'CLE',
    r'Tampa Bay Buccaneers': 'TAM',
    r'Pittsburgh Steelers': 'PIT',
    r'Atlanta Falcons': 'ATL',
    r'Indianapolis Colts': 'IND',
    r'Miami Dolphins': 'MIA',
    r'Green Bay Packers': 'GNB',
    r'Cincinnati Bengals': 'CIN',
    r'Tennessee Titans': 'TEN',
    r'Minnesota Vikings': 'MIN',
    r'(San Diego|Los Angeles) Chargers': 'SDG',
    r'Baltimore Ravens': 'BAL',
    r'Dallas Cowboys': 'DAL',
    r'(St. Louis|Los Angeles) Rams': 'RAM',
    r'Buffalo Bills': 'BUF',
    r'Kansas City Chiefs': 'KAN',
    r'Detroit Lions': 'DET',
    r'Seattle Seahawks': 'SEA',
    r'Philadelphia Eagles': 'PHI',
    r'San Francisco 49ers': 'SFO',
    r'Chicago Bears': 'CHI',
    r'Carolina Panthers': 'CAR',
    r'Denver Broncos': 'DEN',
    r'New York Jets': 'NYJ',
    r'New York Giants': 'NYG',
    r'Washington (Redskins|Football Team|Commanders)': 'WAS',
    r'Arizona Cardinals': 'ARI',
    r'(Oakland|Las Vegas) Raiders': 'RAI'
}

other_regex = {
    r'^(?:[\t ]*(?:\r?\n|\r))+': '',
    r'(\d+)\.(\d+)': r'$1,$2'
}