import sys
from modules import players as pl
from modules import teams
from modules import matches
from modules import core
from modules import tournaments

PLAYER_TEAM = None

def make_new_team():
    global PLAYER_TEAM
    PLAYER_TEAM = teams.Team(input('Enter a team name: '), player_formation_input())
    print('The first team is: \n')
    print(PLAYER_TEAM)


def player_formation_input():
    formation = []
    
    while True:
        try:
            quant_defenders = int(input('Enter the number of defenders: '))
            quant_midfielders = int(input('Enter the number of midfielders: '))
            quant_attackers = int(input('Enter the number of attackers: '))
        except TypeError:
            print('Must be an integer.')
            continue
        else:
            formation = [quant_defenders, quant_midfielders, quant_attackers]
            player_count = 0
            for i in formation:
                player_count += i
            if player_count != 10:
                print('There should be 10 total outfield players.')
                continue
            else:
                print(f"Your formation is {quant_defenders}-{quant_midfielders}-{quant_attackers}")
                return formation


def play_new_team():
    global PLAYER_TEAM
    print('Great, let\'s play!')
    print('Creating opposition...')

    opp_team = teams.Team('Manchester City', [4, 4, 2])

    print('Your opposition is: \n')
    print(opp_team)

    next_match = matches.Match(PLAYER_TEAM, opp_team)
    print('The match will now be played: ' + str(next_match))

    next_match.play_match()
    print('Result: ' + str(next_match))


def play_tournament():
    global PLAYER_TEAM
    print('Great, let\'s play!')
    print('Creating tournament...')

    tournament = tournaments.Tournament(PLAYER_TEAM)

    tournament.play_quarters()
   

print('Welcome to football manager!')

if core.check_input('Would you like to create a new team (y/n)? '):
    make_new_team()
else:
    core.exit_message()
while True:
    if core.check_input('Would you like to play a game with this team (y/n)? '):
        play_tournament()
    elif core.check_input('Would you like to generate a new team (y/n)? '):
        print('Signing new players...')
        make_new_team()
    else:
        core.exit_message() 
