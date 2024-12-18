from stats_team import *
from stats_player import *
from stats_others import *

years = list(range(2012, 2015))
    
#TODO: Criar um README.MD
#TODO: Documentar melhor o código   

# ----------------------------------------------------------------------------------------------------------------------------------
def main():
    create_folders()
    for year in years:
        scraping_rosters(year)
        scraping_gamelogs(year)
        scraping_gamelogs_opp(year)
        scraping_team_stats(year)
        scraping_player_stats(year)
        scraping_others(year)

        move_files(year)

    scraping_images()
    
if __name__ == "__main__":
    main()