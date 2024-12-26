import sys
from modules import players as pl
from modules import teams
from modules import matches
from modules import core

PLAYER_TEAM = None

def make_new_team():
    global PLAYER_TEAM
    PLAYER_TEAM = teams.Team(input('Enter a team name: '))
    print('The first team is: \n')
    print(PLAYER_TEAM)


def play_new_team():
    global PLAYER_TEAM
    print('Great, let\'s play!')
    print('Creating opposition...')

    opp_team = teams.Team('Manchester City')

    print('Your opposition is: \n')
    print(opp_team)

    next_match = matches.Match(PLAYER_TEAM, opp_team)
    print('The match will now be played: ' + str(next_match))

    next_match.play_match()
    print('Result: ' + str(next_match))
   

print('Welcome to football manager!')

if core.check_input('Would you like to create a new team (y/n)? '):
    make_new_team()
else:
    core.exit_message()
while True:
    if core.check_input('Would you like to play a game with this team (y/n)? '):
        play_new_team()
    elif core.check_input('Would you like to generate a new team (y/n)? '):
        print('Signing new players...')
        make_new_team()
    else:
        core.exit_message() 
