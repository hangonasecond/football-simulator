from statistics import mean
from math import ceil
from modules.names import player_name
import pandas as pd
import random as rd

PRIMARY_MIN = 50
PRIMARY_MAX = 90
PRIMARY_WEIGHT = 1.0
SECONDARY_MIN = 30
SECONDARY_MAX = 70
SECONDARY_WEIGHT = 1.3
TERTIARY_MIN = 10
TERTIARY_MAX = 50
TERTIARY_WEIGHT = 1.8


class Player:
    def __init__(self, first_name, last_name, height, weight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.age = age

        self.set_stats()
        self.set_rating()


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


    def set_stats(self):
        self.physical = rd.randint(20, 80)
        self.mental = rd.randint(20, 80)
        self.goalkeeping = 10


    def generate_primary(self):
        return rd.randint(PRIMARY_MIN, PRIMARY_MAX)
    

    def generate_secondary(self):
        return rd.randint(SECONDARY_MIN, SECONDARY_MAX)

    
    def generate_tertiary(self):
        return rd.randint(TERTIARY_MIN, TERTIARY_MAX)

    def format_rating(self):
        stars = ''
        norm_rating = ceil(self.rating/20)

        for i in range(0, norm_rating):
            stars = stars + '*'

        return stars


class Attacker(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)
        self.position = 'ATT'


    def set_stats(self):
        Player.set_stats(self)
        self.defending = self.generate_tertiary()
        self.passing = self.generate_tertiary()
        self.dribbling = self.generate_secondary()
        self.shooting = self.generate_primary()
     

    def set_rating(self):
        self.rating = int(mean([
            PRIMARY_WEIGHT * self.physical,
            PRIMARY_WEIGHT * self.mental,
            TERTIARY_WEIGHT * self.defending,
            TERTIARY_WEIGHT * self.passing,
            SECONDARY_WEIGHT * self.dribbling,
            PRIMARY_WEIGHT * self.shooting
            ]))


class Midfielder(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)
        self.position = 'MID'


    def set_stats(self):
        Player.set_stats(self)
        self.defending = self.generate_tertiary()
        self.passing = self.generate_secondary()
        self.dribbling = self.generate_secondary()
        self.shooting = self.generate_secondary()


    def set_rating(self):
       self.rating = int(mean([
           PRIMARY_WEIGHT * self.physical,
           PRIMARY_WEIGHT * self.mental,
           TERTIARY_WEIGHT * self.defending,
           SECONDARY_WEIGHT * self.passing,
           SECONDARY_WEIGHT * self.dribbling,
           SECONDARY_WEIGHT * self.shooting
           ]))


class Defender(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)
        self.position = 'DEF'


    def set_stats(self):
        Player.set_stats(self)
        self.defending = self.generate_primary()
        self.passing = self.generate_secondary()
        self.dribbling = self.generate_tertiary()
        self.shooting = self.generate_tertiary()
    
    
    def set_rating(self):
        self.rating = int(mean([
            PRIMARY_WEIGHT * self.physical,
            PRIMARY_WEIGHT * self.mental,
            PRIMARY_WEIGHT * self.defending,
            SECONDARY_WEIGHT * self.passing,
            TERTIARY_WEIGHT * self.dribbling,
            TERTIARY_WEIGHT * self.shooting
            ]))


class Goalkeeper(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)
        self.position = 'GK'


    def set_stats(self):
        Player.set_stats(self)
        self.goalkeeping = self.generate_primary()
        self.defending = self.generate_tertiary()
        self.passing = self.generate_tertiary()
        self.shooting = 10
        self.dribbling = 10

    def set_rating(self):
        self.rating = int(mean([
            self.physical,
            self.mental,
            self.goalkeeping
            ]))
 

class Team():
    def __init__(self, name):
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
                players.append(Goalkeeper(names[0], names[1], 200, 90, 32))
            elif i in range(1, 5):
                players.append(Defender(names[0], names[1], 190, 100, 29))
            elif i in range(5, 9):
                players.append(Midfielder(names[0], names[1], 180, 80, 26))
            elif i in range(9, 11):
                players.append(Attacker(names[0], names[1], 150, 100, 22))
            else:
                print('Player out of bounds')
                break
        return players


    def set_rating(self):
        player_ratings = []
        for player in self.players:
            player_ratings.append(player.rating)

        self.rating = int(mean(player_ratings))

