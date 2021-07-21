class MasterView:

    def __init__(self):
        pass

    def get_input(self, prompt):
        user_input = input(prompt + " : ")
        return user_input

    def get_multiple_inputs(self, details):
        user_inputs = []
        for detail in details:
            prompt = detail
            user_input = self.get_input(prompt)
            user_inputs.append(user_input)

        return user_inputs
        pass


class TournamentView(MasterView):

    def __init__(self):
        pass

    def show_tournaments(tournaments):
        for tournament in tournaments:
            print(tournament)
        pass

    def show_tournament(tournament):
        print(tournament)

    def get_input_tournament(details):
        # NOTE maybe a parent class should handle this?
        pass
