from models.player_model import Player
from controllers.player_controller import PlayerController
from views.player_view import MasterView, PlayerView



def main():
    pc = PlayerController(Player, PlayerView)


if __name__ == "__main__":
    main()
