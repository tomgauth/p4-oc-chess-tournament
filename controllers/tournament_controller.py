# This is the tournament controller
from models.player_model import Player
from models.round_model import Round


class TournamentController:

    def __init__(self, tournament_model_handler,
                 player_model_handler, view):
        self.t_model_handler = tournament_model_handler
        self.p_model_handler = player_model_handler
        self.view = view
        self.selected_tournament = None

    def select_tournament(self):
        tournaments = self.t_model_handler.all_tournaments()
        self.show_tournaments()
        selection = self.view.get_input()
        self.selected_tournament = tournaments[selection]
        self.view.show_tournament_details(self.selected_tournament)

    def show_tournaments(self):
        # do something
        list_tournaments = self.t_model_handler.all_tournaments()
        self.view.print_tournaments(list_tournaments)
        return True

    def delete_tournament():
        # prompts tournament name
        # pass to model to destroy the tournament
        # prints("tournament {name} has been deleted")
        pass

    def show_tournament(self, tournament):
        players = []
        for player_id in tournament.players:
            player_obj = self.p_model_handler.search(id_key=player_id)
            players.append(player_obj)
        self.view.show_tournament_details(tournament, players)

    def find_tournament(self, name):
        print(self.tournaments)
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament

    def add_player(self):
        p = Player()
        p.first_name = self.view.get_input('player first name: ')
        # p.last_name = self.view.get_input('player last name: ')
        # p.sex = self.view.get_input('player sex (M/F/O: ')
        # p.ranking = self.view.get_input('player ranking')
        player = self.p_model_handler.save_to_db(p)
        return player.id_key
        # create a player

    def add_players(self):
        added_players = []  # list of player key_ids
        adding_players = ''
        while (adding_players != 'n') and (len(added_players) < 8):
            print('adding_players', adding_players) # loop doesn't break here.
            print(adding_players == 'n')
            added_player_id = self.add_player()
            added_players.append(added_player_id)
            adding_players = self.view.get_input(f'''
            {len(added_players)}/8 players added
            Press "n" to stop adding players
            Press enter to continue''')

        return added_players

    def create_tournament(self):
        t = self.t_model_handler.model
        t.name = self.view.get_input('name')
        # t.location = self.view.get_input('location')
        # t.date_start = self.view.get_input('date_start')
        # t.date_end = self.view.get_input('date_end')
        # t.num_of_rounds = self.view.get_input('num_of_rounds')
        # t.rounds = self.view.get_input('rounds')
        # t.players = self.view.get_input('players')
        # t.time_control = self.view.get_input('time_control')
        t.players = t.players.extend(self.add_players())
        th = self.t_model_handler
        saved_tournament = th.save_to_db(t)
        self.show_tournament(saved_tournament)
        return True
        # from self.model get the attr
        # create a tournament from Model

    def start_tournament(self):
        # this controller will create and manage a tournament
        # create a round

        # t_model_handler.create_round()
        # create matches for the round
        # allow the user to update the results of the matches
        #   - find a player
        #   - update the match where the player participated with the result of the match
        # Generate new matches for the players
        # Update again the results
        pass

    def select(self, selection):
        if selection == '1':
            return self.create_tournament()
        elif selection == '2':
            return self.show_tournaments()
        elif selection == '3':
            print('edit a tournament')
        else:
            print("Invalid Input")

    def select_action(self):
        self.view.display_actions()
        return self.select(self.view.get_input())
