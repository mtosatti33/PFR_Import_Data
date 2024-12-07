from folders import *
from config import *
from files import *
# Files to Move
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