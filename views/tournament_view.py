# A View should never call its own methods. Only a Controller should do it.
class TournamentView():

    def get_input(self, prompt=None):
        if prompt:
            print(prompt)
        user_input = input("=> ")
        return user_input

    def print_tournaments(self, tournaments):
        for i in range(len(tournaments)):
            tournament = tournaments[i]
            print(f"{i} - {tournament.name}")

    def show_tournament_details(self, tournament, players=[]):
        print(f'''TOURNAMENT {tournament.name}
Location: {tournament.location}
Time_control: {tournament.time_control}
PLAYERS: ''')
        for i in range(len(players)):
            player = players[i]
            print(f'''Name: {player.first_name} - {player.last_name}
Ranking: {player.ranking}
      ----        ''')

    def display_actions(self):
        print('''TOURNAMENTS MENU
Select an action:
1. Create a tournament
2. See tournaments
3. Edit a tournament
4. Start a tournament
          ''')
