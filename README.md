# fpl_player-quality-score
## Overview
The purpose of this program is to produce a quality score for Fantasy Premier League elements (players) using Lasso regression coefficients.

## Process

1. (get_player_data.py) 
- Extract weekly data from FPL API and create a dataframe with player stats for each game week and then create seperate dataframes for each position and stored these dataframes in a dictionary
- Extract season total data from FPL API and create dataframes of season totals for each position

2. (get_coefficients.py)
- Run Lasso regression on weekly dataframe for each position and store feature coefficients in the all_coefs dataframe.

3. (quality_scores.py) 
- Calculated the quality score using the feature coefs for each player per position.
- Export player quality scores for most recent week and store in /data
 
## How to use this tool
1. Run quality_score.py
2. Use csv file generated in '/data' directory
