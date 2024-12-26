from random import randint

class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.played = False

    def __str__(self):
        if self.played:
            return f"{self.home_team.name} {self.home_score} - {self.away_score} {self.away_team.name}"
        else:
            return f"{self.home_team.name} v. {self.away_team.name}"

    # choose a random number of possible goal events
    # each event has a chance of either team scoring (or none)
    # based on the home team's relative strength
    def play_match(self):
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

        if self.home_score == self.away_score:
            winner = None
        elif self.home_score > self.away_score:
            winner = self.home_team
        else:
            winner = self.away_team

        self.played = True

    # get the differential between the team's ratings
    # used to determine which team is more likely to win
    # if the home team is stronger than the away team this
    # will be positive, and vice versa
    def rating_diff(self):
        abs_rating_diff = self.home_team.rating - self.away_team.rating
        relative_rating_diff = abs_rating_diff / self.home_team.rating

        return relative_rating_diff
