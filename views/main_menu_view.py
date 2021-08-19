# This is the main menu view
from views.master_view import MasterView


class MainMenuView(MasterView):

    def display_actions(self):
        print('''
MAIN MENU
=========

Select an option:
1. Tournaments
2. Players
3. Quit''')
