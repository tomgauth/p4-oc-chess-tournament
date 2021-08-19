# This is the main menu controller


class MainMenuController:
    def __init__(self, main_menu_view, tournament_controller,
                 player_controller):
        self.mm_view = main_menu_view
        self.t_controller = tournament_controller
        self.p_controller = player_controller

    def select(self, selection):
        if selection == 1:
            return self.t_controller.run()
        elif selection == 2:
            return self.p_controller
        elif selection == 3:
            print("Goodbye")
        else:
            print("Invalid Input")

    def run(self):
        running = True
        while running:
            prompt = self.mm_view.display_actions()
            selection = self.mm_view.sanitised_input(
                prompt, type_=int, range_=[1, 2, 3])
            self.select(selection)
            if selection == 3:
                break
            print("Running MainMenu: ", running)

        # display the main menu with the diffferent options
        # redirect to the corresponding view/menu depending on user input
        # create actions depending on input (pairs players in matches
        # during each round)
