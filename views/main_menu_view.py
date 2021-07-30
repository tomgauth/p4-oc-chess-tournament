# This is the main menu view


class MainMenuView():

    # this method should be inherited from MasterView.
    # TODO: implement inheritance from MasterView
    def get_input(self):
            user_input = input("=> ")
            return user_input

    def display_actions(self):
        print('''Select an option:
1. Tournaments
2. Players
3. Quit''')
