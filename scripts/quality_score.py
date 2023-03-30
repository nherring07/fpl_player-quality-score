import pandas as pd
from get_player_data import season_df, weekly_df
from get_coefficients import get_coefs

print('Calculating quality scores...')

all_coefs = get_coefs()

feat_cols = ['minutes', 'expected_goals_conceded', 'expected_goal_involvements',
       'expected_assists', 'value', 'threat', 'creativity', 'influence',
       'expected_goals']
last_gameweek = max(weekly_df['round'])

totals_df = season_df
totals_cols = ['id','web_name','element_type' ,'total_points','minutes','influence', 'creativity','threat','expected_goals','expected_assists','expected_goal_involvements', 'expected_goals_conceded', 'value_form']
totals_df = totals_df[totals_cols].rename(columns={'value_form':'value'})

quality_scores = []

for i in totals_df.index:
    weighted_values = []
    element_type = totals_df.loc[i]['element_type']
    for c in feat_cols:
        coef = (all_coefs[(all_coefs['feature'] == 'minutes') & (all_coefs['element_type'] == 1)]['lasso_coef'].values).item()
        value = float(totals_df.loc[i][c])
        weighted_value = coef * value
        weighted_values.append(weighted_value)
    qs = sum(weighted_values)
    quality_scores.append({'id': totals_df.loc[i]['id'], 'name': totals_df.loc[i]['web_name'], 'element_type':element_type, 'total_points': totals_df.loc[i]['total_points'], 'quality_score' : qs})

pd.DataFrame(quality_scores).to_csv(f'/Users/herrn/Documents/GitHub/fpl_player-quality-score/data/player_quality_scores_{last_gameweek}')
