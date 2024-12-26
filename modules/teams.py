import pandas as pd
from modules import players as pl
from modules.names import player_name
from statistics import mean

class Team():
    def __init__(self, name):
        self.set_formation()
        self.players = self.generate_players()
        self.name = name;

        self.set_rating()


    def __str__(self):
        team = []

        for player in self.players:
            team.append([
                player.position,
                player.last_name,
                player.format_rating(),
                player.physical,
                player.mental,
                player.defending,
                player.passing,
                player.dribbling,
                player.shooting,
                player.goalkeeping
                ])

        teamsheet = pd.DataFrame(team, index=range(1, (len(team)+1)), columns=['Position', 'Name', 'Rating', 'PHY', 'MEN', 'DEF', 'PAS', 'DRI', 'SHO', 'GK'])
        return self.name + ' (' + str(self.rating) + ')\n' + str(teamsheet)


    def generate_players(self):
        players = []
        for i in range(11):
            names = player_name()
            if i == 0:
                players.append(pl.Goalkeeper(names[0], names[1], 200, 90, 32))
            elif i in range(1, 1 + self.formation[0]):
                players.append(pl.Defender(names[0], names[1], 190, 100, 29))
            elif i in range(1 + self.formation[0], 1 + self.formation[0] + self.formation[1]):
                players.append(pl.Midfielder(names[0], names[1], 180, 80, 26))
            elif i in range(11 - self.formation[2], 11):
                players.append(pl.Attacker(names[0], names[1], 150, 100, 22))
            else:
                print('Player out of bounds')
                break
        return players


    def set_rating(self):
        player_ratings = []
        for player in self.players:
            player_ratings.append(player.rating)

        self.rating = int(mean(player_ratings))

    def set_formation(self):
        self.formation = [4, 4, 2]
