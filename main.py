from models.player_model import Player, PlayerHandler
from models.tournament_model import Tournament, TournamentHandler
from controllers.player_controller import PlayerController
from views.player_view import PlayerView
from tinydb import TinyDB
from controllers.tournament_controller import TournamentController
from views.tournament_view import TournamentView
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController


def main():
    pc = PlayerController(Player, PlayerView)
    # Create TinyDB object
    db = TinyDB('db.json')
    # Create tournament table
    tournaments_table = db.table('tournaments')
    players_table = db.table('players')
    ph = PlayerHandler(players_table)
    main_menu_view = MainMenuView()
    t_view = TournamentView()
    p_view = PlayerView()
    tournament = Tournament()
    th = TournamentHandler(tournaments_table, tournament)
    t_controller = TournamentController(th, ph, t_view)
    p_controller = PlayerController(ph, p_view)
    main_menu_controller = MainMenuController(
        main_menu_view, t_controller, p_controller)

    main_menu_controller.run()


if __name__ == "__main__":
    main()
