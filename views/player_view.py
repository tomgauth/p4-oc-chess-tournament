# This is the player model


class PlayerView:

    def __init__(self):
        pass

    def show_players(players):
        for player in players:
            print(player)
        pass

    def show_player(player):
        print(player.first_name + " " + player.last_name)
        print("ranking:" + player.ranking)
        print("Date of birth" + player.birth_date)

    def get_input_player(details):
        # NOTE maybe a parent class should handle this?
        pass
