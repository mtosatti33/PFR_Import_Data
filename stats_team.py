from urls import *
from scraper import *
from utils import *
from config import *

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_rosters(_year):
    if is_roster_scraped:
        # Scraping Rosters
        for key, value in teams.items():
            url = URL_ROSTER.format(key, _year)
            scraping_data(url,attrs='roster', is_data_append_csv=True, file=f"{value}.csv", is_append_team=True)

        concat_dfs(rosters)

        move_file(rosters, f'{ROSTERS}/{_year}.csv')

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_gamelogs(_year):
    if is_gamelogs_scraped:
        for key, value in teams.items():
            url = URL_TEAM_GAMELOGS.format(key, _year)
            scraping_data(url,attrs=f'gamelog{_year}', file=f"{value}.csv", is_append_team=True)

        concat_dfs(gamelogs)

        move_file(gamelogs, f'{GAMELOGS}/team/{_year}.csv')
        clean_remaining_data()
        
# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_gamelogs_opp(_year):
    if is_gamelogs_opp_scraped:
        for key, value in teams.items():
            url = URL_TEAM_GAMELOGS.format(key, _year)
            scraping_data(url,attrs=f'gamelog_opp{_year}', file=f"{value}.csv", is_append_team=True)

        concat_dfs(gamelogs_opp)

        move_file(gamelogs_opp, f'{GAMELOGS}/opp/{_year}.csv')
        clean_remaining_data()
        
# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_team_stats(_year):
    if is_team_scraped:
        for key, value in team_off_save_dict.items():
            scraping_data(URL_TEAM_OFFENSE.format(_year) ,key, value)

        for key, value in team_def_save_dict.items():
            scraping_data(URL_TEAM_DEFENSE.format(_year) ,key, value)
