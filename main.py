class Player:
    def __init__(self, first_name, last_name, height, weight, age):
        self.first_name = first_name
        self.last_name = last_name,
        self.height = height
        self.weight = weight
        self.age = age

        self.set_stats()

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def set_stats(self):
        self.physical = 50
        self.mental = 50

class Attacker(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.defending = 20
        self.passing = 40
        self.dribbling = 60
        self.shooting = 80


class Midfielder(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.defending = 30
        self.passing = 70
        self.dribbling = 60
        self.shooting = 40


class Defender(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.defending = 80
        self.passing = 60
        self.dribbling = 40
        self.shooting = 20

class Goalkeeper(Player):
    def __init__(self, first_name, last_name, height, weight, age):
        Player.__init__(self, first_name, last_name, height, weight, age)

    def set_stats(self):
        Player.set_stats(self)
        self.goalkeeping = 80
 
class Team():
    def __init__(self):
        self.players = self.generate_players()

    def __str__(self):
        teamsheet = ''

        for player in self.players:
            teamsheet = teamsheet + str(player) + '\n'

        return teamsheet

    def generate_players(self):
        players = []
        for i in range(11):
            print(i)
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

print('Welcome to football manager!')

print('Generating team...')

team_first = Team()

print('The first team is: \n' + str(team_first))
