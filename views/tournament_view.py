# A View should never call its own methods. Only a Controller should do it.
class TournamentView():

    def get_input(self, prompt=None):
        if prompt:
            print(prompt)
        user_input = input("=> ")
        return user_input

    def print_tournaments(self, tournaments):
        for tr in tournaments:
            print("{} - {}".format(tr.doc_id, tr['name']))

    def show_tournament_details(self, tournament):
        print("""TOURNAMENT {}
Location: {}
Time_control: {}""".format(
            tournament['name'],
            tournament['location'], tournament['players']))
        if len(tournament['players']) > 0:
            for player in tournament['players']:
                print("""Name: {} - {}
Ranking: {}
      ----        """.format(player['first_name'], player['last_name'],
                             player['ranking']))

    def display_actions(self):
        print('''TOURNAMENTS MENU
Select an action:
1. Create a tournament
2. See tournaments
3. Edit a tournament
4. Start a tournament
          ''')
