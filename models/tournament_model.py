# This is the tournament model
from models.player_model import Player
from tinydb import TinyDB
db = TinyDB('db.json')


class Tournament:
    def __init__(self, name="", location="", date_start="",
                 date_end="", num_of_rounds=4, rounds=[], players=[],
                 time_control="", description=""):
        self.t_table = db.table('tournaments')
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.num_of_rounds = num_of_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description

    def create_tournament(self):
        return self.t_table.insert(
            {"name": self.name,
             "location": self.location,
             "date_start": self.date_start,
             "date_end": self.date_end,
             "num_of_rounds": self.num_of_rounds,
             "rounds": self.rounds,
             "players": self.players,
             "time_control": self.time_control,
             "description": self.description
             })

    def get_from_id(self, id_num):
        data = self.t_table.get(doc_id=id_num)
        new_tournament = Tournament(
            name=data["name"],
            location=data["location"],
            date_start=data["date_start"],
            date_end=data["date_end"],
            num_of_rounds=data["num_of_rounds"],
            rounds=data["rounds"],
            players=data["players"],
            time_control=data["time_control"],
            description=data["description"]
        )
        for player_id in data["players"]:
            player_data = Player.get_from_id(player_id)
            player = Player(
                last_name=player_data['last_name'],
                first_name=player_data['first_name'],
                birth_date=player_data['birth_date'],
                sex=player_data['sex'],
                ranking=player_data['ranking']
            )
            new_tournament.add_player(player)
        return new_tournament

    def add_player(self, player):
        self.players.append(player)

    def read_tournament(self, id_num):
        """ find a tournament by id """
        """ check how to get object by id in tinydb """
        return self.t_table.get(doc_id=id_num)

    def read_tournaments(self):
        """ returns all tournaments """
        return self.t_table.all()

    def update_tournament(self, id_num, obj):
        return self.t_table.update(obj, doc_ids=[id_num])

    def delete_touranment(self, id_num):
        return self.t_table.remove(doc_ids=[id_num])
