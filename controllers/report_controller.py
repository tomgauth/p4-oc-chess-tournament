# this is the report controller


class ReportController:
    def __init__(self, player_model, tournament_model, tournament_controller,
                 report_view):
        self.p_model = player_model
        self.t_model = tournament_model
        self.t_controller = tournament_controller
        self.report_view = report_view

    def list_players(self, players='all', mode='alpha'):
        if players == 'all':
            players = self.p_model.read_players()
        if mode == 'ranking':
            players = self.t_controller.sort_players_by_ranking(players)
        else:
            players = sorted(
                players, key=lambda x: (x.last_name, x.first_name),
                reverse=False)

        self.report_view.show_players(players)

    def list_players_ranking(self):
        self.list_players(mode='ranking')

    def list_players_tournament(self, mode='alpha'):
        selected_tournament = self.t_controller.select_tournament()
        players = selected_tournament.players
        self.list_players(players, mode=mode)

    def list_players_tournament_ranking(self):
        self.list_players_tournament(mode='ranking')

    def all_tournaments(self):
        self.t_controller.show_tournaments()

    def tournament_rounds(self):
        selected_tournament = self.t_controller.select_tournament()
        rounds = selected_tournament.rounds
        self.report_view.show_rounds(rounds)

    def tournament_matches(self):
        selected_tournament = self.t_controller.select_tournament()
        matches = selected_tournament.matches()
        for match in matches:
            match_players = match.players()
            self.report_view.show_match(match, match_players)

    def select(self, selection):
        switcher = {
            1: self.list_players,
            2: self.list_players_ranking,
            3: self.list_players_tournament,
            4: self.list_players_tournament_ranking,
            5: self.all_tournaments,
            6: self.tournament_rounds,
            7: self.tournament_matches
        }
        func = switcher.get(selection, lambda: "Invalid input")
        func()

    def run(self):
        while True:
            self.report_view.display_actions()
            selection = self.report_view.sanitised_input(
                "=>", type_=int,
                range_=[1, 2, 3, 4, 5, 6, 7, 8])
            self.select(selection)
            if selection == 8:
                break
