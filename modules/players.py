from statistics import mean
from math import ceil
from scipy.stats import truncnorm
import random as rd

PRIMARY_MIN = 50
PRIMARY_MAX = 90
PRIMARY_MEAN = 60
PRIMARY_WEIGHT = 1.0
SECONDARY_MIN = 30
SECONDARY_MAX = 70
SECONDARY_MEAN = 40
SECONDARY_WEIGHT = 1.3
TERTIARY_MIN = 10
TERTIARY_MAX = 50
TERTIARY_MEAN = 30
TERTIARY_WEIGHT = 1.8
STAT_SD = 30


class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.set_stats()
        self.set_rating()


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


    def set_stats(self):
        a_trunc = 20
        b_trunc = 80
        a = (a_trunc - 60) / 10
        b = (b_trunc - 60) / 10
        self.physical = int(truncnorm.rvs(a, b, loc = 60, scale = 20))
        self.mental = int(truncnorm.rvs(a, b, loc = 60, scale = 20))
        self.goalkeeping = 10


    def generate_primary(self):
        a = (PRIMARY_MIN - PRIMARY_MEAN) / STAT_SD
        b = (PRIMARY_MAX - PRIMARY_MEAN) / STAT_SD
        return int(truncnorm.rvs(a, b, loc = PRIMARY_MEAN, scale = STAT_SD))

    def generate_secondary(self):
        a = (SECONDARY_MIN - SECONDARY_MEAN) / STAT_SD
        b = (SECONDARY_MAX - SECONDARY_MEAN) / STAT_SD
        return int(truncnorm.rvs(a, b, loc = SECONDARY_MEAN, scale = STAT_SD))

    
    def generate_tertiary(self):
        a = (TERTIARY_MIN - TERTIARY_MEAN) / STAT_SD
        b = (TERTIARY_MAX - TERTIARY_MEAN) / STAT_SD
        return int(truncnorm.rvs(a, b, loc = TERTIARY_MEAN, scale = STAT_SD))


    def format_rating(self):
        stars = ''
        norm_rating = ceil(self.rating/20)

        for i in range(0, norm_rating):
            stars = stars + '*'

        return stars


class Attacker(Player):
    def __init__(self, first_name, last_name):
        Player.__init__(self, first_name, last_name)
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
    def __init__(self, first_name, last_name):
        Player.__init__(self, first_name, last_name)
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
    def __init__(self, first_name, last_name):
        Player.__init__(self, first_name, last_name)
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
    def __init__(self, first_name, last_name):
        Player.__init__(self, first_name, last_name)
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
