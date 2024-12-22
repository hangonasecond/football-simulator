import sys
import players as pl
from check_input import check_input

print('Welcome to football manager!')

if check_input('Would you like to create a new team (y/n)? '):
    team_first = pl.Team()
    print('The first team is: \n')
    print(team_first)
else:
    print('Alright. Thanks for trying football manager.')
    sys.exit()


