# This is the player controller
from models.player_model import Player


class PlayerController:

    def __init__(self, player_model, view):
        self.p_model = player_model
        self.view = view

    def select_player(self):
        all_players = self.p_model.read_players()
        players_ids = []
        for player in all_players:
            players_ids.append(player.id)
        selection = self.view.sanitised_input('enter player id => ', type_=int,
                                              range_=players_ids)
        player = Player()
        selected_player = player.get_player_from_id(selection)
        return selected_player

    def edit_player(self):
        self.show_players()
        selected_player = self.select_player()
        sp = selected_player
        self.view.custom_message("press enter to keep the previous value")
        view = self.view.sanitised_input
        sp.first_name = view('player first name: ', type_=str.capitalize,
                             len_min=2, default=sp.first_name)
        sp.last_name = view('player last name: ', type_=str.capitalize,
                            len_min=2, default=sp.last_name)
        sp.sex = view('player sex (M/F/O): ', type_=str.upper,
                      range_=['M', 'F', 'O'], default=sp.sex)
        sp.birth_date = view(
            'player birth date (ddmmyyy): ', type_=str, len_min=8, len_max=8,
            default=sp.birth_date)

        sp.ranking = view('player ranking: ', type_=int, min_=0, max_=4000,
                          default=sp.ranking)
        sp.save_player()
        self.view.custom_message('Modified Player')
        self.view.show_player(sp)

    def show_players(self):
        # do something
        all_players = self.p_model.read_players()
        self.view.print_players(all_players)
        return all_players

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

    def back_to_main(self):
        print("Back to Main Menu")

    def select(self, selection):
        switcher = {
            1: self.show_players,
            2: self.edit_player,
            3: self.back_to_main
        }
        func = switcher.get(selection, lambda: "Invalid input")
        func()

    def run(self):
        while True:
            self.view.display_actions()
            selection = self.view.sanitised_input("=>", type_=int,
                                                  range_=[1, 2, 3])
            self.select(selection)
            if selection == 3:
                break
