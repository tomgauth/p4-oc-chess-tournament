# This is the tournament controller
class TournamentController:

    def __init__(self, model_handler, model, view):
        self.model_handler = model_handler
        self.model = model
        self.view = view

    def create_tournament(self):
        self.model.name = self.view.get_input("name")
        self.model.location = self.view.get_input("location")
        self.model.date_start = self.view.get_input("date_start")
        self.model.date_end = self.view.get_input("date_end")
        self.model.num_of_rounds = self.view.get_input("num_of_rounds")
        self.model.rounds = self.view.get_input("rounds")
        self.model.players = self.view.get_input("players")
        self.model.time_control = self.view.get_input("time_control")
        self.model.description = self.view.get_input("description")

        self.model_handler.save(self.model)

        # from tournament view
        # Prompt user for first_name, birth_date, sex, ranking
        # get last_name, first_name, birth_date, sex, ranking
        # create a tournament object from the model
        # tournamentView.message(
        # "tournament {last_name} {first_name} has been created")
        pass

    def show_tournaments(self):
        # do something
        self.view.show_tournaments(self.tournaments)

    def delete_tournament():
        # prompts tournament name
        # pass to model to destroy the tournament
        # prints("tournament {name} has been deleted")
        pass

    def show_tournament_details(self):
        first_name = self.view.get_input("first name")
        last_name = self.view.get_input("last name")
        tournament = self.find_tournament(first_name, last_name)
        self.view.show_tournament(tournament)

    def find_tournament(self, first_name, last_name):
        print(self.tournaments)
        for tournament in self.tournaments:
            if tournament.first_name == first_name and tournament.last_name == last_name:
                return tournament

    def test_tournament(self):
        print("Tournament controller test")
        self.model.test()
