import pandas as pd
from get_player_data import season_df,weekly_df
from get_coefficients import all_coefs

feat_cols = all_coefs.feature.unique()
last_gameweek = max(weekly_df['round'])

totals_df = season_df
totals_cols = ['id','web_name','element_type' ,'minutes','influence', 'creativity','threat','expected_goals','expected_assists','expected_goal_involvements', 'expected_goals_conceded', 'value_form']
totals_df = totals_df[totals_cols].rename(columns={'value_form':'value'})

quality_scores = []

for i in totals_df.index:
    weighted_values = []
    element_type = totals_df.loc[i]['element_type']
    for c in feat_cols:
        coef = float(all_coefs[(all_coefs['feature'] == c) & (all_coefs['element_type'] == element_type)]['lasso_coef'].values)
        value = float(totals_df.loc[i][c])
        weighted_value = coef * value
        weighted_values.append(weighted_value)
    qs = sum(weighted_values)
    quality_scores.append({'id': totals_df.loc[i]['id'], 'name': totals_df.loc[i]['web_name'], 'element_type':element_type, 'total_points': totals_df.loc[i]['total_points'], 'quality_score' : qs})

pd.DataFrame(quality_scores).to_csv(f'data/player_quality_scores_{last_gameweek}')
