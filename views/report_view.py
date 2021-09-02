# this is the report view
from views.master_view import MasterView


class ReportView():

    def show_players(self, players):
        for player in players:
            print(""" {} - {}
Ranking: {}
----------------""".format(
                player.last_name, player.first_name, player.ranking))

    def show_rounds(self, rounds):
        for round_ in rounds:
            print("""
{}
{} - {}
""".format(round_.name, round_.date_time_start, round_.date_time_end))

    def show_match(self, match, players):
        p1 = players[0]
        p2 = players[0]
        print("""
{} {} vs {} {}
Score:      {} - {}
-----------------------""".format(
            p1.first_name, p1.last_name, p2.first_name, p2.last_name,
            match.p1_score, match.p2_score))

    def display_actions(self):
        print('''
REPORTS MENU
================

Select an action:
1. Show all players (alphabetically)
2. Show all players (by ranking)
3. Show all players of a tournament (alphabetically)
4. Show all players of a tournament (by ranking)
5. Show all tournaments
6. Show all rounds of a tournament
7. Show all matches of a tournament
8. Back to main menu
          ''')
