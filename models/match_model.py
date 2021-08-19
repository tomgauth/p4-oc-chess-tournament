# This is the match model
from tinydb import TinyDB
db = TinyDB('db.json')
from models.player_model import Player


class Match:
    def __init__(self, p1_id='', p1_score='', p2_id='', p2_score=''):
        self.m_table = db.table('matches')
        self.p1_id = p1_id
        self.p1_score = p1_score
        self.p2_id = p2_id
        self.p2_score = p2_score
        self.id = ''

    # call a function that gets the self.id

    def tuple(self):
        return ([self.p1_id, self.p1_score], [self.p2_id, self.p2_score])

    def create_match(self):
        match_id = self.m_table.insert({
            'p1_id': self.p1_id,
            'p1_score': self.p1_score,
            'p2_id': self.p2_id,
            'p2_score': self.p2_score
        })
        return self.m_table.update({'id': match_id}, doc_ids=[match_id])[0]

    def save_match(self):
        if self.id == '':
            result = self.create_match()
        else:
            result = self.m_table.update(
                {'p1_id': self.p1_id,
                 'p1_score': self.p1_score,
                 'p2_id': self.p2_id,
                 'p2_score': self.p2_score,
                 'id': self.id
                 }, doc_ids=[self.id])[0]
        return result

    def players(self):
        players = []
        players.append(Player.get_player_from_id(self.p1_id))
        players.append(Player.get_player_from_id(self.p2_id))
        return players

    def p1_won(self):
        self.p1_score = 1
        self.p2_score = 0

    def p2_won(self):
        self.p1_score = 0
        self.p2_score = 1

    def tie(self):
        self.p1_score = 0.5
        self.p2_score = 0.5

    @staticmethod
    def get_match_from_id(id_num):
        match = Match()
        match_data = match.m_table.get(doc_id=int(id_num))
        match.p1_id = match_data["p1_id"]
        match.p1_score = match_data["p1_score"]
        match.p2_id = match_data["p2_id"]
        match.p2_score = match_data["p2_score"]
        match.id = id_num
        return match

    def read_match(self, id_num):
        """ find a match by id """
        """ check how to get object by id in tinydb """
        return self.m_table.get(doc_id=id_num)

    def read_matches(self):
        """ returns all matches """
        return self.m_table.all()

    def update_match(self, id_num, obj):
        return self.m_table.update(obj, doc_ids=[id_num])

    def delete_match(self, id_num):
        return self.m_table.remove(doc_ids=[id_num])


"""
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
chacune contenant deux éléments : une référence à une instance de joueur et un score.
Les matches multiples doivent être stockés sous forme de liste sur l'instance du tour.
"""
