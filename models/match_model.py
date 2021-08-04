class Match:
    def __init__(self, player_one, player_two,
                 p1_score=None, p2_score=None):
        self.p1 = player_one
        self.p1_score = p1_score
        self.p2 = player_two
        self.p2_score = p2_score

    def match(self):
        return ([self.p1, self.p1_score], [self.p2, self.p2_score])
