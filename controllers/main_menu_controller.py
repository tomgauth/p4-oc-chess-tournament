# This is the main menu controller


class MainMenuController:
    def __init__(self, main_menu_view, tournament_controller,
                 player_controller, report_controller):
        self.mm_view = main_menu_view
        self.t_controller = tournament_controller
        self.p_controller = player_controller
        self.report_controller = report_controller

    def goodbye(self):
        print("Goodbye")

    def select(self, selection):
        switcher = {
            1: self.t_controller.run,
            2: self.p_controller.run,
            3: self.report_controller.run,
            4: self.goodbye
        }
        func = switcher.get(selection, lambda: "Invalid input")
        func()

    def run(self):
        while True:
            self.mm_view.display_actions()
            selection = self.mm_view.sanitised_input(
                '=>', type_=int, range_=[1, 2, 3, 4])
            self.select(selection)
            if selection == 4:
                break
