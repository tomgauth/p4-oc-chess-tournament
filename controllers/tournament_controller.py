# This is the tournament controller
from models.player_model import Player
from models.round_model import Round


class TournamentController:

    def __init__(self, tournament_model, player_model, view):
        self.t_model = tournament_model
        self.p_model = player_model
        self.view = view
        self.selected_tournament = None

    def select_tournament(self):
        tournaments = self.t_model.all_tournaments()
        self.show_tournaments()
        selection = int(self.view.get_input())
        self.selected_tournament = tournaments[selection]
        self.view.show_tournament_details(self.selected_tournament)
        return self.selected_tournament

    def show_tournaments(self):
        # do something
        list_tournaments = self.t_model.read_tournaments()
        self.view.print_tournaments(list_tournaments)
        return True

    def delete_tournament():
        # prompts tournament name
        # pass to model to destroy the tournament
        # view shows ("tournament {name} has been deleted")
        pass

    def show_tournament(self, tournament):
        players = []
        for player_id in tournament['players']:
            player = self.p_model.read_player(player_id)
            players.append(player)
        self.view.show_tournament_details(tournament, players)

    def find_tournament(self, name):
        print(self.tournaments)
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament

    def add_player(self):
        self.p_model.first_name = self.view.get_input('player first name: ')
        # p.last_name = self.view.get_input('player last name: ')
        # p.sex = self.view.get_input('player sex (M/F/O: ')
        # p.ranking = self.view.get_input('player ranking')
        player_id = self.p_model.create_player()
        return player_id
        # create a player

    def add_players(self):
        added_players = []  # list of player key_ids
        while len(added_players) < 8:
            player_id = self.add_player()
            added_players.append(player_id)
            print('added_players : ', len(added_players), '/8')
        return added_players

    def create_tournament(self):
        """ create a new Tournament() object
            for each value, gets input from the view
            add the value to the tournament
            ask model to create_tournament() to save
        """
        t = self.t_model
        t.name = self.view.get_input('name')
        # t.location = self.view.get_input('location')
        # t.date_start = self.view.get_input('date_start')
        # t.date_end = self.view.get_input('date_end')
        # t.num_of_rounds = self.view.get_input('num_of_rounds')
        # t.rounds = self.view.get_input('rounds')
        # t.time_control = self.view.get_input('time_control')
        added_players = self.add_players()
        print('create_tournament() added_players : ', added_players)
        t.players.extend(added_players)
        print("t_players : ", t.players)
        tournament_id = t.create_tournament()
        created_tournament = self.t_model.read_tournament(tournament_id)
        print("SAVED TOURNMANET", created_tournament)
        self.show_tournament(created_tournament)
        return True
        # from self.model get the attr
        # create a tournament from Model

    def start_tournament(self):
        # this controller will create and manage a tournament
        selected_tournament = self.select_tournament()
        # create a round

        # r = Round()
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
        elif selection == '4':
            return self.start_tournament()
        else:
            print("Invalid Input")

    def select_action(self):
        self.view.display_actions()
        return self.select(self.view.get_input())