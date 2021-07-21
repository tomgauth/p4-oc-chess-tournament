# This is the main menu controller


class MainMenuController:
    def __init__(self, view, tournament_controller):
        self.view = view
        self.tc = tournament_controller

    def start(self):
        self.view.show_main_menu()

    def select_option(self):
        selection = self.view.get_input('''Select an option:
                                        1 - Create new tournament
                                        2 - Manage tournaments''')

        self.redirect(selection)

    def redirect(self, selection):
        if selection == '1':
            self.tc.create_tournament()
            # create new tournament
            # call tournament_controller
