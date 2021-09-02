# This is the player model
from views.master_view import MasterView


class PlayerView(MasterView):

    def print_players(self, players):
        for player in players:
            print("ID:{} {} - {}".format(player.id, player.first_name,
                                         player.last_name,
                                         ))

    def show_player(self, player):
        print("""
{} - {} {}
Ranking: {}
Date of Birth: {}
Sex: {}
          """.format(
            player.id, player.first_name, player.last_name, player.ranking,
            player.birth_date, player.sex))

    def display_actions(self):
        print('''
PLAYERS MENU
============

Select an action:
1. See all players
2. Edit a player
3. Back to main menu
          ''')
