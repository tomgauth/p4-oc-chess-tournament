# A View should never call its own methods. Only a Controller should do it.
from views.master_view import MasterView


class TournamentView(MasterView):

    def get_input(self, prompt=None):
        self.sanitised_input(prompt)

    def print_tournaments(self, tournaments):
        print("""
TOURNAMENTS
===========""")
        for tr in tournaments:
            print("{} - {}".format(tr.id, tr.name))

    def show_tournament_details(self, tournament, players):
        print("""TOURNAMENT {}
Location: {}
Time_control: {}""".format(
            tournament.name,
            tournament.location, tournament.time_control))
        if len(tournament.players) > 0:
            for player in players:
                print("""Name: {} - {}
Ranking: {}
      ----        """.format(player.first_name, player.last_name,
                             player.ranking))

    def show_round_details(self, round_):
        print("""{}
date time start: {}
date time end:   {}

MATCHES:
          """.format(
            round_.name, round_.date_time_start,
            round_.date_time_end))
        for match in round_.matches:
            players = match.players()
            p1 = players[0]
            p2 = players[1]
            print("""
{} {} vs {} {}
Score:      {} - {}
-----------------------""".format(
                p1.first_name, p1.last_name, p2.first_name, p2.last_name,
                match.p1_score, match.p2_score))

    def pick_match_winner(self, match):
        players = match.players()
        p1 = players[0]
        p2 = players[1]
        print("""
{} {} vs {} {}
Score:      {} - {}
-----------------------""".format(
            p1.first_name, p1.last_name, p2.first_name, p2.last_name,
            match.p1_score, match.p2_score))
        print("""WHO WON?
1 - {} {} Won
2 - {} {} Won
3 - Tie""".format(p1.first_name, p1.last_name, p2.first_name, p2.last_name))

    def show_ranked_players(self, sorted_players, tournament):
        for idx, p in enumerate(sorted_players):
            position = idx+1
            p.score = p.current_score(tournament)
            print("""{} - [{}] {} {} """.format(
                position, p.score, p.first_name, p.last_name))

    def display_actions(self):
        print('''
TOURNAMENTS MENU
================

Select an action:
1. Create a tournament
2. See tournaments
3. Edit a tournament
4. Start a tournament
5. Back to main menu
          ''')
