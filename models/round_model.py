# This is the round model
from models.match_model import Match
from tinydb import TinyDB
db = TinyDB('db.json')


class Round:
    def __init__(self, matches=[]):
        self.r_table = db.table('rounds')
        self.matches = []

    def create_round(self):
        return self.r_table.insert({"matches": self.matches})

    def get_round_from_id(self, id_num):
        round_data = self.r_table.get(doc_id=id_num)
        print(round_data)
        round_ = Round()
        print(round_)
        for match_id in round_data["matches"]:
            print(match_id)
            match = Match().get_match_from_id(match_id)
        round_.matches.add_match(match)

        return round_

    def add_match(self, match):
        self.matches.append(match.tuple())

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
