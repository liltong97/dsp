# coding: utf-8
# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import pandas as pd
filepath = '/Users/lilliantong/ds/metis/metisgh/prework/dsp/python/football.csv'
df = pd.read_csv(filepath)
goals = df['Goals']
goals_allowed = df['Goals Allowed']
difference = abs(goals - goals_allowed)
index_of_min = difference.idxmin()
print(index_of_min)
names = df['Team']
print names[index_of_min]


