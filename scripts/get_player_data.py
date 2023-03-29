import pandas as pd
import requests

def get_player_data(timeframe):
    #import data from FPL API endpoint
    data = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json()

    
    #extract relevant columns and player IDs
    players_df = pd.DataFrame(data['elements']).dropna(axis=1)
    players_df = players_df[players_df.minutes > 0]
    players_attr_df = players_df[['id','web_name','element_type','team',]]
    player_ids = players_df['id']

    if timeframe == 'season':
        return players_df
    elif timeframe == 'weekly':
        #create empty dataframe to store weekly player data
        weekly_df = pd.DataFrame()
        #loop through all player IDs, download their weekly data, and append the data ro the weekly_df
        for pid in player_ids:
            weekly_data = requests.get(f'https://fantasy.premierleague.com/api/element-summary/{pid}/').json()
            weekly_player_df = pd.DataFrame(weekly_data['history'])
            weekly_df = pd.concat([weekly_df,weekly_player_df],ignore_index=True)

        #add player details from players_df and reorganize columns
        weekly_df = weekly_df.merge(players_attr_df, how='left', left_on='element',right_on='id')
        weekly_df = weekly_df.reindex(columns=['element', 'web_name', 'element_type', 'team','fixture', 'opponent_team', 'total_points', 'was_home',
            'kickoff_time', 'team_h_score', 'team_a_score', 'round', 'minutes',
            'goals_scored', 'assists', 'clean_sheets', 'goals_conceded',
            'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards',
            'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity',
            'threat', 'ict_index', 'starts', 'expected_goals', 'expected_assists',
            'expected_goal_involvements', 'expected_goals_conceded', 'value',
            'transfers_balance', 'selected', 'transfers_in', 'transfers_out'])
        return weekly_df

    
weekly_df = get_player_data('weekly')
season_df = get_player_data('season')