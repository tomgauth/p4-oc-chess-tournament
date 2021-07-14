# This is the player model


class MasterView:

    def __init__(self):
        pass

    def get_input(prompt):
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


class PlayerView(MasterView):

    def __init__(self):
        pass

    def show_players(players):
        for player in players:
            print(player)
        pass

    def show_player(player):
        print(player.first_name + " " + player.last_name)
        print("ranking:" + player.ranking)
        print("Date of birth" + player.birth_date)

    def get_input_player(details):
        # NOTE maybe a parent class should handle this?
        pass
