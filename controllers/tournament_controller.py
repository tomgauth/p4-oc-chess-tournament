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

    def select_tournament(self, show=False):
        self.show_tournaments()
        selection = int(self.view.get_input())
        tournament = Tournament()
        selected_tournament = tournament.get_tournament_from_id(selection)
        if show:
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

    def start_round(self, tournament, round_):
        if round_.name == 'Round1':
            print('round1')
            players = self.sort_players_by_ranking(tournament.players)

            for i in range(int(len(players)/2)):
                match = round_.matches[i]
                match.p1_id = players[i].get_player_id()
                match.p2_id = players[i+4].get_player_id()
                match.save_match()

            round1 = round_
            round1.start_round()
            # show round1
            self.view.show_round_details(round1)

            while True:
                status = self.view.get_input('type "END" to close the round')
                if not status == 'END':
                    continue
                else:
                    break
            round1.finish_round()

            for match in round1.matches:
                result = self.view.pick_match_winner(match)
                if result == '1':
                    match.p1_won()
                if result == '2':
                    match.p2_won()
                if result == '3':
                    match.tie()
                else:
                    print('wrong input')
                match.save_match()
            self.view.show_round_details(round1)
        else:
            while True:
                status = self.view.get_input(
                    'type "START" to start {}'.format(round_.name))
                if not status == 'START':
                    continue
                else:
                    break

            srtd_players = sorted(
                tournament.players, key=lambda x: (x.current_score(tournament),
                                                   x.ranking), reverse=True)
            print('srtd_players: ', srtd_players)

            """ special case for player 1 """

            p1 = srtd_players[0]
            srtd_players.remove(p1)
            if srtd_players[0] in p1.played_against(tournament):
                p2 = srtd_players[1]
            else:
                p2 = srtd_players[0]
            srtd_players.remove(p2)
            match = round_.matches[0]
            match.p1_id = p1.id
            match.p2_id = p2.id
            match.save_match()

            """ create the matches for the other players """
            i = 1
            while len(srtd_players) > 0:
                p1 = srtd_players[0]
                srtd_players.remove(p1)
                p2 = srtd_players[0]
                srtd_players.remove(p2)
                match = round_.matches[i]
                match.p1_id = p1.id
                match.p2_id = p2.id
                match.save_match()
                i += 1

            round_.start_round()
            self.view.show_round_details(round_)

            while True:
                status = self.view.get_input('type "END" to close the round')
                if not status == 'END':
                    continue
                else:
                    break
            round_.finish_round()
            for match in round_.matches:
                result = self.view.pick_match_winner(match)
                if result == '1':
                    match.p1_won()
                if result == '2':
                    match.p2_won()
                if result == '3':
                    match.tie()
                else:
                    print('wrong input')
                match.save_match()
            self.view.show_round_details(round_)

    def start_tournament(self):
        # this controller will create and manage a tournament
        tournament = self.select_tournament()
        # move this function to the round controller?
        for round_ in tournament.rounds:
            self.start_round(tournament, round_)

        # sort the players by score
        srtd_players = sorted(
            tournament.players, key=lambda x: x.current_score(tournament),
            reverse=True)

        self.view.show_ranked_players(srtd_players, tournament)

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
