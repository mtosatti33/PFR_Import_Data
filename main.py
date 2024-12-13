from urls import *
from functions import *
from config import *
#TODO: Criar um README.MD
#TODO: Documentar melhor o código
# ----------------------------------------------------------------------------------------------------------------------------------
def recreate():
    recreate_folders()

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_rosters():
    if is_roster_scraped:
        # Scraping Rosters
        for key, value in teams.items():
            url = URL_ROSTER.format(key, year)
            scraping_data(url,attrs='roster', is_data_append_csv=True, file=f"{value}.csv", is_append_team=True)

        concat_dfs()
        
# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_team_stats():
    if is_team_scraped:
        for key, value in team_off_save_dict.items():
            scraping_data(URL_TEAM_OFFENSE.format(year) ,key, value)

        for key, value in team_def_save_dict.items():
            scraping_data(URL_TEAM_DEFENSE.format(year) ,key, value)

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_player_stats():
    if is_player_scraped:
        # Player Stats
        scraping_data(URL_PASSING.format(year),'passing', player_passing, is_data_append_csv=True)
        scraping_data(URL_RUSHING.format(year),'rushing', player_rushing, is_data_append_csv=True)
        scraping_data(URL_RECEIVING.format(year),'receiving', player_receiving, is_data_append_csv=True)
        scraping_data(URL_DEFENSE.format(year),'defense', player_defense, is_data_append_csv=True)
        scraping_data(URL_KICKING.format(year),'kicking', player_kicking, is_data_append_csv=True)
        scraping_data(URL_PUNTING.format(year),'punting', player_punting, is_data_append_csv=True)
        scraping_data(URL_RETURNS.format(year),'returns', player_returns, is_data_append_csv=True)

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_general_data():
    if is_season_scraped:
        # Drafts
        scraping_data(URL_DRAFT.format(year), 'drafts', draft, is_data_append_csv=True)

        # Awards
        if is_finished:
            scraping_data(URL_ALL_PRO.format(year), 'all_pro', AP, is_data_append_csv=True)
            scraping_data(URL_PRO_BOWL.format(year), 'pro_bowl', PB, is_data_append_csv=True)

        # Coaches
        scraping_data(URL_COACHES.format(year), 'coaches', coaches)

        # Schedules
        scraping_data(URL_SCHEDULES.format(year), 'games', games)


# ----------------------------------------------------------------------------------------------------------------------------------
def main():
    recreate()
    scraping_rosters()
    scraping_team_stats()
    scraping_player_stats()
    scraping_general_data()
    move_files()

if __name__ == "__main__":
    main()