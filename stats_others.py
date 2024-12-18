from urls import *
from scraper import *
from utils import *
from config import *

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_others(_year):
    if is_season_scraped:
        # Drafts
        scraping_data(URL_DRAFT.format(_year), 'drafts', draft, is_data_append_csv=True)

        # Awards
        if is_finished:
            scraping_data(URL_ALL_PRO.format(_year), 'all_pro', AP, is_data_append_csv=True)
            scraping_data(URL_PRO_BOWL.format(_year), 'pro_bowl', PB, is_data_append_csv=True)

        # Coaches
        scraping_data(URL_COACHES.format(_year), 'coaches', coaches)

        # Schedules
        scraping_data(URL_SCHEDULES.format(_year), 'games', games)

# ----------------------------------------------------------------------------------------------------------------------------------
def scraping_images():
    if is_images_downloaded:

        if not os.path.exists(TEAM_LOGOS):
            create_folder(TEAM_LOGOS)

            for key, value in teams.items():
                url = URL_TEAM.format(key, 2024)
                download_logo(url=url, _team=value)

            url = URL_LEAGUE.format(2024)
            download_logo(url=url)

