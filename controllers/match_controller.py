class MatchController:
    def __init__(self, match_model):
        self.match = match_model

    def player1_wins(self):
        self.match.p1_score = 1
        self.match.p2_score = 0

    def player2_wins(self):
        self.match.p1_score = 0
        self.match.p2_score = 1

    def tie(self):
        self.match.p1_score = 0.5
        self.match.p2_score = 0.5
