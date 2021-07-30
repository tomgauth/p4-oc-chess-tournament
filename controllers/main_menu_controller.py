# This is the main menu controller


class MainMenuController:
    def __init__(self, main_menu_view, tournament_controller, player_controller):
        self.mm_view = main_menu_view
        self.t_controller = tournament_controller
        self.p_controller = player_controller

    def select(self, selection):
        if selection == '1':
            return self.t_controller.select_action()
        elif selection == '2':
            return self.p_controller
        elif selection == '3':
            return False
        else:
            print("Invalid Input")

    def run(self):
        running = True
        while running:
            self.mm_view.display_actions()
            running = self.select(self.mm_view.get_input())
            print("Running: ", running)


        # display the main menu with the diffferent options
        # redirect to the corresponding view/menu depending on user input
        # create actions depending on input (pairs players in matches
        # during each round)

