from urls import *
from functions import *
from items import *
from config import *
from files import *


def recreate():
    if not os.path.exists('data'):
        recreate_folders()

def scraping_rosters():
    # Scraping Rosters
    for key, value in teams.items():
        url = URL_ROSTER.format(key, year)
        scraping_data(url,attrs='roster', is_data_append_csv=True, file=f"{value}.csv", is_append_team=True)

    concat_dfs()

def scraping_team_stats():
    for key, value in team_off_save_dict.items():
        scraping_data(URL_TEAM_OFFENSE.format(year) ,key, value)

    for key, value in team_def_save_dict.items():
        scraping_data(URL_TEAM_DEFENSE.format(year) ,key, value)

    # Advanced
    # ----------------------------------------------------------------------------------------------------------------------------------
    # Passing
    scraping_data(URL_TEAM_ADV_OFFENSE.format(year),'air_yards', team_adv_air_yards)
    scraping_data(URL_TEAM_ADV_OFFENSE.format(year),'accuracy', team_adv_accuracy, data_show='.assoc_accuracy')
    scraping_data(URL_TEAM_ADV_OFFENSE.format(year),'pressure', team_adv_pressure, data_show='.assoc_pressure')
    scraping_data(URL_TEAM_ADV_OFFENSE.format(year),'play_type', team_adv_play_type, data_show='.assoc_play_type')

    # Rushing, Receiving, Defense
    scraping_data(URL_TEAM_ADV_OFFENSE.format(year),'advanced_rushing', team_adv_rushing)
    scraping_data(URL_TEAM_ADV_OFFENSE.format(year),'advanced_receiving', team_adv_receiving)
    scraping_data(URL_TEAM_DEFENSE.format(year),'advanced_defense', team_adv_defense)

def scraping_player_stats():
    # Player Stats
    scraping_data(URL_PASSING.format(year),'passing', player_passing, is_data_append_csv=True)
    scraping_data(URL_RUSHING.format(year),'rushing', player_rushing, is_data_append_csv=True)
    scraping_data(URL_RECEIVING.format(year),'receiving', player_receiving, is_data_append_csv=True)
    scraping_data(URL_DEFENSE.format(year),'defense', player_defense, is_data_append_csv=True)
    scraping_data(URL_KICKING.format(year),'kicking', player_kicking, is_data_append_csv=True)
    scraping_data(URL_PUNTING.format(year),'punting', player_punting, is_data_append_csv=True)
    scraping_data(URL_RETURNS.format(year),'returns', player_returns, is_data_append_csv=True)

    # Advanced
    # ----------------------------------------------------------------------------------------------------------------------------------
    # Passing
    scraping_data(URL_ADV_PASSING.format(year),'passing_advanced', player_adv_passing, is_data_append_csv=True)

    # Rushing, receiving and defense
    scraping_data(URL_ADV_RUSHING.format(year),'adv_rushing', player_adv_rushing, is_data_append_csv=True)
    scraping_data(URL_ADV_RECEIVING.format(year),'adv_receiving', player_adv_receiving, is_data_append_csv=True)
    scraping_data(URL_ADV_DEFENSE.format(year),'defense_advanced', player_adv_defense, is_data_append_csv=True)

def scraping_general_data():
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

def move():
    move_files()

    clean_remaining_data()

if __name__ == "__main__":
    recreate()
    scraping_rosters()
    scraping_team_stats()
    scraping_player_stats()
    scraping_general_data()
    move()
