# This is the player model
from tinydb import TinyDB
db = TinyDB('db.json')


class Player:
    def __init__(self, last_name='', first_name='', birth_date='',
                 sex='', ranking=''):
        self.p_table = db.table('players')
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.ranking = ranking

    def create_player(self):
        return self.p_table.insert(
            {"last_name": self.last_name,
             "first_name": self.first_name,
             "birth_date": self.birth_date,
             "sex": self.sex,
             "ranking": self.ranking
             })

    def get_from_id(self, id_num):
        player_data = self.p_table.get(doc_id=id_num)
        return player_data

    def read_player(self, id_num):
        """ find a player by id """
        """ check how to get object by id in tinydb """
        return self.p_table.get(doc_id=id_num)

    def read_players(self):
        """ returns all players """
        return self.p_table.all()

    def update_player(self, id_num, obj):
        return self.p_table.update(obj, doc_ids=[id_num])

    def delete_touranment(self, id_num):
        return self.p_table.remove(doc_ids=[id_num])
