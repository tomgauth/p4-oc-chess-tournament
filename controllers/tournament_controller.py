# This is the tournament controller
from models.tournament_model import Tournament
from models.player_model import Player
from models.round_model import Round
from models.match_model import Match


class TournamentController:

    def __init__(self, tournament_model, player_model, view):
        self.t_model = tournament_model
        self.p_model = player_model
        self.view = view

    def select_tournament(self):
        self.show_tournaments()
        selection = int(self.view.get_input())
        tournament = Tournament()
        selected_tournament = tournament.get_tournament_from_id(selection)
        self.show_tournament(selected_tournament)
        return selected_tournament

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
        players = tournament.players
        self.view.show_tournament_details(tournament, players)

    def find_tournament(self, name):
        print(self.tournaments)
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament

    def add_player(self):
        self.p_model.first_name = self.view.get_input('player first name: ')
        # self.p_model.last_name = self.view.get_input('player last name: ')
        # self.p_model.sex = self.view.get_input('player sex (M/F/O): ')
        # self.p_model.birth_date = self.view.get_input(
        #     'player birth date (DD/MM/YYYY): ')
        # self.p_model.ranking = int(self.view.get_input('player ranking'))
        player_id = self.p_model.save_player()
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
        t.location = self.view.get_input('location')
        t.date_start = self.view.get_input('date_start')
        t.date_end = self.view.get_input('date_end')
        t.time_control = self.view.get_input('time_control')
        added_players = self.add_players()
        print('create_tournament() added_players : ', added_players)
        t.players = added_players
        print("t_players : ", t.players)
        tournament_id = t.create_tournament()
        created_tournament = Tournament.get_tournament_from_id(tournament_id)
        print("SAVED TOURNMANET", created_tournament)
        self.show_tournament(created_tournament)
        return True
        # from self.model get the attr
        # create a tournament from Model

    def sort_players_by_ranking(self, players):
        srtd_players = sorted(players, key=lambda x: x.ranking, reverse=False)
        return srtd_players

    def start_tournament(self):
        # this controller will create and manage a tournament
        tournament = self.select_tournament()
        # move this function to the player controller?
        players = self.sort_players_by_ranking(tournament.players)

        for i in range(int(len(players)/2)):
            match = tournament.rounds[0].matches[i]
            match.p1_id = players[i].get_player_id()
            match.p2_id = players[i+4].get_player_id()
            match.save_match()

        # do not create new matches, populate existing matches
        # change the line below to get updated matches (from id?)

        return tournament  # todo remove later

        """
        allow the user to update the results of the matches
          - find a player
          - update the match where the player participated with the result of
        the match
        Generate new matches for the players
        Update again the results
        """

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
