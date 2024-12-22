import pandas as pd
import random as rd

PRIMARY_MIN = 50
PRIMARY_MAX = 90
SECONDARY_MIN = 30
SECONDARY_MAX = 70
TERTIARY_MIN = 10
TERTIARY_MAX = 50

class Player:
    def __init__(self, first_name, last_name, height, weight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.age = age

        self.set_stats()

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

class Attacker(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.defending = self.generate_tertiary()
        self.passing = self.generate_tertiary()
        self.dribbling = self.generate_secondary()
        self.shooting = self.generate_primary()

class Midfielder(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.defending = self.generate_tertiary()
        self.passing = self.generate_secondary()
        self.dribbling = self.generate_secondary()
        self.shooting = self.generate_secondary()

class Defender(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.defending = self.generate_primary()
        self.passing = self.generate_secondary()
        self.dribbling = self.generate_tertiary()
        self.shooting = self.generate_tertiary()

class Goalkeeper(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.goalkeeping = self.generate_primary()
        self.defending = self.generate_tertiary()
        self.passing = self.generate_tertiary()
        self.shooting = 10
        self.dribbling = 10
 
class Team():
    def __init__(self, name):
        self.players = self.generate_players()
        self.name = name;

    def __str__(self):
        team = []

        for player in self.players:
            team.append([
                player.last_name,
                player.physical,
                player.mental,
                player.defending,
                player.passing,
                player.dribbling,
                player.shooting,
                player.goalkeeping
                ])

        teamsheet = pd.DataFrame(team, index=range(1, (len(team)+1)), columns=['Name', 'PHY', 'MEN', 'DEF', 'PAS', 'DRI', 'SHO', 'GK'])
        return str(teamsheet)

    def generate_players(self):
        players = []
        for i in range(11):
            if i == 0:
                players.append(Goalkeeper('Iker', 'Casillas', 200, 90, 32))
            elif i in range(1, 5):
                players.append(Defender('Mr.', 'Defender', 190, 100, 29))
            elif i in range(5, 9):
                players.append(Midfielder('Mr.', 'Midfielder', 180, 80, 26))
            elif i in range(9, 11):
                players.append(Attacker('Messi', 'Ronaldo', 150, 100, 22))
            else:
                print('Player out of bounds')
                break
        return players

