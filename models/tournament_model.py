# This is the tournament model
from tinydb import Query
import json


class Tournament:
    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])

        # self.name = name  # None
        # self.location = location  # None
        # self.date_start = date_start  # None
        # self.date_end = date_end  # None  # default same as date_start
        # self.num_of_rounds = num_of_rounds  # 4  # default 4
        # self.rounds = rounds  # []  # list of instances 'rounds'
        # self.players = players  # []
        # self.time_control = time_control  # None  # bullet, blitz, rapid
        # self.description = description  # None


class TournamentHandler:
    def __init__(self, tournaments_table):
        self.tour_db = tournaments_table

    def save(self, tournament):
        return self.tour_db.insert(tournament.__dict__)

    def all(self):
        return self.tour_db.all()

    def get_tournament_by_name(self, tournament_name):
        return self.tour_db.get(Query().name == tournament_name)

    def deserialize(self, json_obj):
        return {
            "name": json_obj['name'],
            "location": json_obj['location'],
            "date_start": json_obj['date_start'],
            "date_end": json_obj['date_end'],
            "num_of_rounds": json_obj['num_of_rounds'],
            "rounds": json_obj['rounds'],
            "players": json_obj['players'],
            "time_control": json_obj['time_control'],
            "description": json_obj['description']
        }
