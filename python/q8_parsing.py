# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd 

fb = pd.read_csv('/Users/eastblue/ds/metis/metisgh/prework/dsp/python/football.csv')

fb['GoalsDiff'] = abs(fb['Goals'] - fb['Goals Allowed'])
smalld = fb.sort_values(by='GoalsDiff')

print('Team with smallest goals difference: ' + str(smalld.iloc[0,0]))