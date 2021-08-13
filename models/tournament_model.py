# This is the tournament model
from models.player_model import Player
from models.round_model import Round
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
        rounds_ids = self.generate_rounds()
        return self.t_table.insert(
            {"name": self.name,
             "location": self.location,
             "date_start": self.date_start,
             "date_end": self.date_end,
             "num_of_rounds": self.num_of_rounds,
             "rounds": rounds_ids,
             "players": self.players,
             "time_control": self.time_control,
             "description": self.description
             })

    def get_tournament_from_id(self, id_num):
        data = self.t_table.get(doc_id=int(id_num))
        new_tournament = Tournament(
            name=data["name"],
            location=data["location"],
            date_start=data["date_start"],
            date_end=data["date_end"],
            num_of_rounds=data["num_of_rounds"],
            time_control=data["time_control"],
            description=data["description"]
        )
        for player_id in data["players"]:
            print("player_id: ", player_id)
            player = Player().get_player_from_id(player_id)
            new_tournament.add_player(player)

        for round_id in data["rounds"]:
            print("round_id: ", round_id)
            round_ = Round().get_round_from_id(round_id)
            new_tournament.add_round(round_)

        return new_tournament

    def generate_rounds(self):
        rounds_ids = []
        for i in range(self.num_of_rounds):
            r = Round()
            r.generate_matches()
            round_id = r.create_round(i+1)
            rounds_ids.append(round_id)
        return rounds_ids

    def add_player(self, player):
        self.players.append(player)

    def matches(self):
        matches = []
        for round_ in self.rounds:
            matches.extend(round_.matches)
        return matches

    def add_round(self, round_):
        self.rounds.append(round_)

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
