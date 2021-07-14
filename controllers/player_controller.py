# This is the player controller
class PlayerController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.players = []

    def create_player():
        # from Player view
        # Prompt user for first_name, birth_date, sex, ranking
        # get last_name, first_name, birth_date, sex, ranking
        # create a player object from the model
        # PlayerView.message(
        # "player {last_name} {first_name} has been created")
        pass

    def show_players(self):
        # do something
        self.view.show_players(self.players)

    def delete_player():
        # prompts player name
        # pass to model to destroy the player
        # prints("player {name} has been deleted")
        pass

    def show_player_details(self):
        first_name = self.view.get_input("first name")
        last_name = self.view.get_input("last name")
        player = self.find_player(first_name, last_name)
        self.view.show_player(player)

    def find_player(self, first_name, last_name):
        print(self.players)
        for player in self.players:
            if player.first_name == first_name and player.last_name == last_name:
                return player

