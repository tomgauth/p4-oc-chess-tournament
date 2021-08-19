# This is the round model
from datetime import datetime
from models.match_model import Match
from tinydb import TinyDB
db = TinyDB('db.json')


class Round:
    def __init__(
            self, matches=None, name='', date_time_start='',
            date_time_end=''):
        self.r_table = db.table('rounds')
        self.matches = matches
        self.name = name
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.id = ''

    def date_time_now(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def finish_round(self):
        self.date_time_end = self.date_time_now()

    def start_round(self):
        self.date_time_start = self.date_time_now()

    def create_round(self, round_num):
        self.name = "Round{}".format(round_num)
        self.matches = self.generate_matches()
        round_id = self.r_table.insert({
            "matches": self.matches,
            "name": self.name,
            "date_time_start": self.date_time_start,
            "date_time_end": self.date_time_end})
        return self.r_table.update({'id': round_id}, doc_ids=[round_id])[0]

    def save_round(self):
        if self.id == '':
            result = self.create_round()
        else:
            result = self.r_table.update(
                {"matches": self.matches,
                 "name": self.name,
                 "date_time_start": self.date_time_start,
                 "date_time_end": self.date_time_end,
                 'id': self.id
                 }, doc_ids=[self.id])[0]
        return result

    @staticmethod
    def get_round_from_id(id_num):
        round_ = Round()
        round_data = round_.r_table.get(doc_id=int(id_num))
        print(round_data)
        round_.name = round_data['name']
        round_.date_time_start = round_data['date_time_start']
        round_.date_time_end = round_data['date_time_end']
        print(round_.name)
        round_.matches = []
        for match_id in round_data["matches"]:
            print(match_id)
            match = Match.get_match_from_id(match_id)
            round_.matches.append(match)

        return round_

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
