# This is the main menu controller


class MainMenuController:
    def __init__(self, main_menu_view, tournament_controller,
                 player_controller, report_controller):
        self.mm_view = main_menu_view
        self.t_controller = tournament_controller
        self.p_controller = player_controller
        self.report_controller = report_controller

    def select(self, selection):
        if selection == 1:
            self.t_controller.run()
        elif selection == 2:
            self.p_controller.run()
        elif selection == 3:
            self.report_controller.run()
        elif selection == 4:
            print("Goodbye")
        else:
            print("Invalid Input")

    def run(self):
        running = True
        while running:
            self.mm_view.display_actions()
            selection = self.mm_view.sanitised_input(
                '=>', type_=int, range_=[1, 2, 3, 4])
            self.select(selection)
            if selection == 4:
                break
