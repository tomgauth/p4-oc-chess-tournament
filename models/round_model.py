# This is the round model
from models.match_model import Match
from tinydb import TinyDB
db = TinyDB('db.json')
from datetime import datetime


class Round:
    def __init__(self, matches=[]):
        self.r_table = db.table('rounds')
        self.matches = []
        self.name = ''
        self.date_time_start = ''
        self.date_time_end = ''

    def date_time_now(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def finish_round(self):
        self.date_time_end = self.date_time_now()

    def start_round(self):
        self.date_time_start = self.date_time_now()

    """TODO: handle save if round already exists """
    def create_round(self, round_num):
        name = "Round{}".format(round_num)
        matches_ids = self.generate_matches()
        return self.r_table.insert({
            "matches": matches_ids,
            "name": name})

    def get_round_from_id(self, id_num):
        round_data = self.r_table.get(doc_id=int(id_num))
        print(round_data)
        round_ = Round()
        print(round_)
        for match_id in round_data["matches"]:
            print(match_id)
            match = Match().get_match_from_id(match_id)
            self.add_match(round_, match)

        return round_

    # should not add it to self, but to the object
    @staticmethod
    def add_match(round_, match):
        round_.matches.append(match)

    def generate_matches(self):
        matches_ids = []
        for i in range(4):
            match_id = Match().create_match()
            matches_ids.append(match_id)
        return matches_ids

    def read_round(self, id_num):
        """ find a round by id """
        """ check how to get object by id in tinydb """
        return self.r_table.get(doc_id=id_num)

    def read_rounds(self):
        """ returns all rounds """
        return self.r_table.all()

    def update_round(self, id_num, obj):
        return self.r_table.update(obj, doc_ids=[id_num])

    def delete_round(self, id_num):
        return self.r_table.remove(doc_ids=[id_num])
