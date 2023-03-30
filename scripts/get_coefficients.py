import pandas as pd
from sklearn.linear_model import Lasso
from get_player_data import weekly_df

def get_coefs():

    print('Calculating coefficients...')
    #create weekly dataframes for each position type
    gkp_df = weekly_df[weekly_df.element_type == 1] 
    def_df = weekly_df[weekly_df.element_type == 2] 
    mid_df = weekly_df[weekly_df.element_type == 3] 
    fwd_df = weekly_df[weekly_df.element_type == 4]

    position_dfs = {1: {'df': gkp_df, 'position':'gkp','element_type': 1}, 2: {'df': def_df, 'position':'def','element_type': 2}, 3: { 'df': mid_df,'position':'mid','element_type': 3}, 4: {'df': fwd_df,'position':'fwd','element_type': 4}}

    #Run lasso regression for each position and store feature coefficients in dataframe

    feat_cols = ['minutes','influence', 'creativity','threat','expected_goals','expected_assists','expected_goal_involvements', 'expected_goals_conceded', 'value']
    lasso = Lasso()
    all_coefs = pd.DataFrame()

    for i in position_dfs:
        X = position_dfs[i]['df'][feat_cols].values
        y = position_dfs[i]['df']['total_points'].values
        position = position_dfs[i]['position']
        element_type = position_dfs[i]['element_type']
        lasso_coef = lasso.fit(X,y).coef_
        this_df = pd.DataFrame({'feature':feat_cols,'lasso_coef': lasso_coef,'element_type': element_type, 'position':position})
        all_coefs = pd.concat([all_coefs,this_df], ignore_index=True).sort_values(by='element_type')

    return all_coefs
