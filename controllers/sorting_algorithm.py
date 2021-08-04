# This is the tournament controller
from models.round_model import Round
from models.match_model import Match
import random


class SortingAlgorithm:
    def __init__(self, tournament):
        self.tournament = tournament

    # initiated with a specific tournament

    # creates a round

    # create matches in the round
    def create_first_round(self):
        r = Round()
        i = 0
        players = self.tournament.players
        random.shuffle(players)
        while i < len(players):
            m = Match(player_one=players[i], player_two=players[i+1])
            r.matches.append(m)
            i += 2
        return r

    def create_round(self):
        # sort the matches depending on the results

        pass

    pass
