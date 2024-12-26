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

    def play_match(self):
        self.home_score = randint(0,5)
        self.away_score = randint(0,5)

        if self.home_score == self.away_score:
            winner = None
        elif self.home_score > self.away_score:
            winner = self.home_team
        else:
            winner = self.away_team

        self.played = True

    # get the differential between the team's ratings
    # used to determine which team is more likely to win
    def rating_diff(self):
        return self.home_team.rating - self.away_team.rating
