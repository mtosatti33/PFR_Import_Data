from urls import *
from scraper import *
from config import *

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_player_stats(_year):
    if is_player_scraped:
        # Player Stats
        scraping_data(URL_PASSING.format(_year),'passing', player_passing, is_data_append_csv=True)
        scraping_data(URL_RUSHING.format(_year),'rushing', player_rushing, is_data_append_csv=True)
        scraping_data(URL_RECEIVING.format(_year),'receiving', player_receiving, is_data_append_csv=True)
        scraping_data(URL_DEFENSE.format(_year),'defense', player_defense, is_data_append_csv=True)
        scraping_data(URL_KICKING.format(_year),'kicking', player_kicking, is_data_append_csv=True)
        scraping_data(URL_PUNTING.format(_year),'punting', player_punting, is_data_append_csv=True)
        scraping_data(URL_RETURNS.format(_year),'returns', player_returns, is_data_append_csv=True)
