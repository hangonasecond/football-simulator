from modules import matches
from modules import teams

TEAM_NAMES = [
    'Manchester City FC',
    'Manchester United FC',
    'Liverpool FC',
    'Tottenham Hotspurs FC',
    'Chelsea FC',
    'Everton FC',
    'Aston Villa FC'
    ]

class Tournament:
    def __init__(self, player_team):
        global TEAM_NAMES
        self.player_team = player_team
        self.teams = [player_team]

        for name in TEAM_NAMES:
            self.teams.append(teams.Team(name, [4, 4, 2]))


    def play_quarters(self):
        quarters = []
        winners = []

        for i in range(0, 4):
            quarters.append([self.teams[2*i], self.teams[2*i + 1]])

        for match in quarters:
            if match[0] == self.player_team:
                print('Your opponent in the quarter finals is: \n')
                print(str(match[1]))

            next_match = matches.Match(match[0], match[1])
            print(str(next_match))
            input('Press Enter to continue... \n')
            
            next_match.play_match(knockout=True)
            print('Result: ' + str(next_match))
            winners.append(next_match.winner)
            input('Press Enter to continue... \n')

        self.quarter_winners = winners
        return self.quarter_winners
            

    def play_semis(self):
        semis = []
        winners = []

        for i in range (0, 2):
            semis.append([self.quarter_winners[2*i], self.quarter_winners[2*i+1]])

        for match in semis:
            if match[0] == self.player_team:
                print('Your opponent in the semi finals is: \n')
                print(str(match[1]))

            next_match = matches.Match(match[0], match[1])
            print(str(next_match))
            input('Press Enter to continue... \n')

            next_match.play_match(knockout=True)
            print('Result: ' + str(next_match))
            winners.append(next_match.winner)
            input('Press Enter to continue... \n')

        self.semi_winners = winners
        return self.semi_winners


    def play_final(self):
        teams = self.semi_winners
        if teams[0] == self.player_team:
            print('Your opponent in the final is: \n')
            print(str(teams[1]))

        final = matches.Match(teams[0], teams[1])
        print(str(final))
        input('Press Enter to continue... \n')

        final.play_match(knockout=True)
        print('Result: ' + str(final))
        
        self.winner = final.winner
        return self.winner
