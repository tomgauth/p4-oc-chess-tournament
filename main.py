from models.player_model import Player
from models.tournament_model import Tournament
from controllers.player_controller import PlayerController
from views.player_view import PlayerView
from tinydb import TinyDB
from controllers.tournament_controller import TournamentController
from views.tournament_view import TournamentView
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController


def main():
    # pc = PlayerController(Player, PlayerView)
    # Create TinyDB object
    db = TinyDB('db.json')
    # Create tournament table
    tournaments_table = db.table('tournaments')
    # players_table = db.table('players')
    player_model = Player()
    main_menu_view = MainMenuView()
    t_view = TournamentView()
    p_view = PlayerView()
    t_model = Tournament(tournaments_table)
    t_controller = TournamentController(t_model, t_view)
    p_controller = PlayerController(player_model, p_view)
    main_menu_controller = MainMenuController(
        main_menu_view, t_controller, p_controller)

    main_menu_controller.run()


if __name__ == "__main__":
    main()
