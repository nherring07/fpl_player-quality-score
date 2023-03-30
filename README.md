# fpl_player-quality-score
## Overview
The purpose of this program is to produce a quality score for Fantasy Premier League elements (players) using Lasso regression coefficients.

## Process
1. Extracted weekly data from FPL API and created a dataframe with player stats for each game week and then created seperate dataframes for each position and stored these dataframes in a dictionary.
2. Ran Lasso regression for each position and store feature coefficients in a dataframe.
3. Extracted season total data from FPL API and created dataframes of season totals for each position. 
4. Calculated the quality score using the feature coefs for each player per position.
5. Export player quality scores for most recent week and store in /data
 
## How to use this tool
-> Run quality_score.py
-> Use csv file generated in '/data' directory
