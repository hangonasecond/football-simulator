import sys
import players as pl
import core

print('Welcome to football manager!')

if core.check_input('Would you like to create a new team (y/n)? '):
    player_team = pl.Team()
    print('The first team is: \n')
    print(player_team)
else:
    core.exit_message()

if core.check_input('Would you like to play a game with this team (y/n)? '):
    print('Great, let\'s play!')
    print('Creating opposition...')

    opp_team = pl.Team()

    print('Your opposition is: \n')
    print(opp_team)
elif core.check_input('Would you like to generate a new team (y/n)? '):
    print('Signing new players...')
    player_team = pl.Team()
else:
    core.exit_message() 
