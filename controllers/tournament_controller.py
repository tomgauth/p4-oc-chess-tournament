# This is the tournament controller
from models.tournament_model import Tournament
from models.player_model import Player
from models.round_model import Round
from models.match_model import Match
from controllers.main_menu_controller import MainMenuController


class TournamentController:

    def __init__(self, tournament_model, player_model, view):
        self.t_model = tournament_model
        self.p_model = player_model
        self.view = view

    def select_tournament(self, show=False):
        all_tournaments = self.show_tournaments()
        tournaments_ids = []
        for tournament in all_tournaments:
            tournaments_ids.append(tournament.id)
        selection = self.view.sanitised_input('=> ', type_=int,
                                              range_=tournaments_ids)
        tournament = Tournament()
        selected_tournament = tournament.get_tournament_from_id(selection)
        if show:
            self.show_tournament(selected_tournament)
        return selected_tournament

    def show_tournaments(self):
        # do something
        all_tournaments = self.t_model.read_tournaments()
        self.view.print_tournaments(all_tournaments)
        return all_tournaments

    def show_tournament(self, tournament):
        players = tournament.players
        self.view.show_tournament_details(tournament, players)

    def find_tournament(self, name):
        print(self.tournaments)
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament

    def add_player(self):
        p = self.p_model
        view = self.view.sanitised_input
        p.first_name = view('player first name: ', type_=str.capitalize,
                            len_min=2)
        p.last_name = view('player last name: ', type_=str.capitalize,
                           len_min=2)
        p.sex = view('player sex (M/F/O): ', type_=str.upper,
                     range_=['M', 'F', 'O'])
        p.birth_date = view(
            'player birth date (ddmmyyy): ', type_=str, len_min=8, len_max=8)

        p.ranking = view('player ranking: ', type_=int, min_=0, max_=4000)
        player_id = p.save_player()
        return player_id

    def add_players(self):
        added_players = []  # list of player key_ids
        while len(added_players) < 8:
            player_id = self.add_player()
            added_players.append(player_id)
            print('added_players : ', len(added_players), '/8')
        return added_players

    def create_tournament(self):
        t = self.t_model
        view = self.view.sanitised_input
        t.name = view('name: ', type_=str, len_min=2)
        t.location = view('location: ', type_=str)
        t.num_of_rounds = view('number of rounds (4 by default): ', type_=int,
                               min_=1,
                               default=4)
        t.date_start = view('date start (ddmmyyyy) ', type_=str, len_min=8,
                            len_max=8)
        t.date_end = view('date end (ddmmyyyy) (default same as date start) ',
                          type_=str, len_min=8, default=t.date_start,
                          len_max=8)
        t.time_control = view('time_control: (bullet, blitz or rapid) ',
                              type_=str.lower,
                              range_=['bullet', 'blitz', 'rapid'])
        t.description = view('description: ', type_=str)
        added_players = self.add_players()
        t.players = added_players
        tournament_id = t.save_tournament()
        created_tournament = Tournament.get_tournament_from_id(tournament_id)
        self.show_tournament(created_tournament)
        return True

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

            self.view.sanitised_input(
                'type "END" to close the round: ', type_=str.upper,
                range_=['END'])

            round1.finish_round()

            for match in round1.matches:
                self.view.pick_match_winner(match)
                result = self.view.sanitised_input("type 1,2 or 3: ",
                                                   type_=int,
                                                   range_=[1, 2, 3])
                if result == 1:
                    match.p1_won()
                if result == 2:
                    match.p2_won()
                if result == 3:
                    match.tie()
                match.save_match()

            self.view.show_round_details(round1)
        else:

            self.view.sanitised_input(
                'type "START" to start {}: '.format(round_.name),
                type_=str.upper, range_=['START'])

            srtd_players = sorted(
                tournament.players, key=lambda x: (x.current_score(tournament),
                                                   x.ranking), reverse=True)

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

            self.view.sanitised_input(
                'type "END" to close the round: ', type_=str.upper,
                range_=['END'])

            round_.finish_round()
            for match in round_.matches:
                self.view.pick_match_winner(match)
                result = self.view.sanitised_input('type 1,2 or 3: ',
                                                   type_=int,
                                                   range_=[1, 2, 3])
                if result == 1:
                    match.p1_won()
                if result == 2:
                    match.p2_won()
                if result == 3:
                    match.tie()

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
        if selection == 1:
            return self.create_tournament()
        elif selection == 2:
            return self.show_tournaments()
        elif selection == 3:
            print('edit a tournament')
        elif selection == 4:
            return self.start_tournament()
        elif selection == 5:
            print("Back to Main Menu")

    def run(self):
        running = True
        while running:
            self.view.display_actions()
            selection = self.view.sanitised_input("=>", type_=int,
                                                  range_=[1, 2, 3, 4, 5])
            self.select(selection)
            if selection == 5:
                break

