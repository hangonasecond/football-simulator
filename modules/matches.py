from random import randint
from modules import goal_events

class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.played = False
        self.penalties = False

    def __str__(self):
        if self.played and self.penalties:
            return f"{self.home_team.name} {self.home_score} ({self.home_penalty}) - ({self.away_penalty}) {self.away_score} {self.away_team.name}"
        elif self.played:
            return f"{self.home_team.name} {self.home_score} - {self.away_score} {self.away_team.name}"
        else:
            return f"{self.home_team.name} v. {self.away_team.name}"

    # choose a random number of possible goal events
    # each event has a chance of either team scoring (or none)
    # based on the home team's relative strength
    def play_match(self, knockout=False):
        self.home_score = 0
        self.away_score = 0

        prob_home_score = 0.5 + self.rating_diff()
        # min and max possible goal events
        # @TODO: adjust this so that expected number of goals is around 3-5
        # can be achieved by adjusting goal events, or scoring probability
        # per event
        num_goal_events = randint(0, 10)

        # P = 0.5 that no goal is scored
        # P = 0.5 that a goal is scored, with the chance that it is scored
        # by the home team impacted by prob_home_score
        for i in range(0, num_goal_events):
            if randint(0, 1) == 1:
                continue
            elif randint(0, 100) / 100 <= prob_home_score:
                self.home_score += 1
            else:
                self.away_score += 1

        if self.home_score == self.away_score and knockout == False:
            self.winner = None
        elif self.home_score == self.away_score and knockout == True:
            print(str(self) + ' has ended in a draw at full time. Now, onto penalties!')
            self.winner = self.penalty_shootout()
            self.penalties = True
        elif self.home_score > self.away_score:
            self.winner = self.home_team
        else:
            self.winner = self.away_team

        self.played = True

    # get the differential between the team's ratings
    # used to determine which team is more likely to win
    # if the home team is stronger than the away team this
    # will be positive, and vice versa
    def rating_diff(self):
        abs_rating_diff = self.home_team.rating - self.away_team.rating
        relative_rating_diff = abs_rating_diff / self.home_team.rating

        return relative_rating_diff


    # called when a knockout match ends in a draw
    # compare a sequence of attackers to the opposition goalkeeper to determine
    # whether a goal is scored
    # winner is either best of 5 or whoever is ahead after each shot thereafter
    def penalty_shootout(self):
        shot_count = 0
        home_keeper = self.home_team.players[0]
        away_keeper = self.away_team.players[0]
        self.home_penalty = 0
        self.away_penalty = 0

        print(home_keeper.last_name + ' steps up in goals for ' + self.home_team.name)
        print(away_keeper.last_name + ' steps up in goals for ' + self.away_team.name)

        while True:
            for i in range(10, -1, -1):
                home_shooter = self.home_team.players[i]
                away_shooter = self.away_team.players[i]

                if goal_events.penalty(att=home_shooter, gk=away_keeper):
                    print(f'{home_shooter.last_name} ({home_shooter.position} {home_shooter.rating}) scores a penalty!')
                    self.home_penalty += 1
                if goal_events.penalty(att=self.away_team.players[i], gk=home_keeper):
                    print(f'{away_shooter.last_name} ({away_shooter.position} {away_shooter.rating}) scores a penalty!')
                    self.away_penalty += 1
                print(f'{self.home_team.name} {self.home_penalty} - {self.away_penalty} {self.away_team.name}')
                shot_count += 1
    
                # declare a winner once the losing team can no longer win a best of 5
                # or when, after a shot is taken, a team has won
                if shot_count in [3, 4]:
                    if self.home_penalty - self.away_penalty > 5 - self.home_penalty:
                        return self.home_team
                    elif self.away_penalty - self.home_penalty > 5 - self.away_penalty:
                        return self.away_team
                elif shot_count >= 5:
                    if self.home_penalty > self.away_penalty:
                        return self.home_team
                    elif self.away_penalty > self.home_penalty:
                        return self.away_team
