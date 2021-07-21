# This is the main menu view


class MainMenuView():

    def show_main_menu(self):
        print('''WELCOME''')

    # this method should be inherited from MasterView.
    # TODO: implement inheritance from MasterView
    def get_input(self, prompt):
            user_input = input(prompt + " : ")
            return user_input
