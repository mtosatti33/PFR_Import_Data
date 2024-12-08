# TODO: aprimorar a estrutura do dicionário para reutilização
# Lista de Times
from files import *

teams = {
    'buf': 'BUF', 'mia': 'MIA', 'nwe': 'NWE', 'nyj': 'NYJ',
    'pit': 'PIT', 'rav': 'BAL', 'cin': 'CIN', 'cle': 'CLE',
    'htx': 'HOU', 'clt': 'IND', 'oti': 'TEN', 'jax': 'JAX', 
    'kan': 'KAN', 'sdg': 'LAC', 'den': 'DEN', 'rai': 'RAI',
    'phi': 'PHI', 'was': 'WAS', 'dal': 'DAL', 'nyg': 'NYG',
    'det': 'DET', 'min': 'MIN', 'gnb': 'GNB', 'chi': 'CHI',
    'atl': 'ATL', 'tam': 'TAM', 'nor': 'NOR', 'car': 'CAR',
    'crd': 'ARI', 'ram': 'LAR', 'sea': 'SEA', 'sfo': 'SFO'
}

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
