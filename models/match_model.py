# This is the match model
from tinydb import TinyDB
db = TinyDB('db.json')
m_table = db.table('matches')


class Match:
    def __init__(self, p1_id='', p1_score='', p2_id='', p2_score=''):
        self.m_table = db.table('matches')
        self.p1_id = p1_id
        self.p1_score = p1_score
        self.p2_id = p2_id
        self.p2_score = p2_score

    def tuple(self):
        return ([self.p1_id, self.p1_score], [self.p2_id, self.p2_score])

    def create_match(self):
        return self.m_table.insert({
            'p1_id': self.p1_id,
            'p1_score': self.p1_score,
            'p2_id': self.p2_id,
            'p2_score': self.p2_score
        })

    @staticmethod
    def get_match_from_id(id_num):
        match_data = m_table.get(doc_id=id_num)
        print(match_data)
        match = Match(
            p1_id=match_data["p1_id"],
            p1_score=match_data["p1_score"],
            p2_id=match_data["p2_id"],
            p2_score=match_data["p2_score"]
        )
        return match

    def read_match(self, id_num):
        """ find a match by id """
        """ check how to get object by id in tinydb """
        return self.m_table.get(doc_id=id_num)

    def read_matchs(self):
        """ returns all matchs """
        return self.m_table.all()

    def update_match(self, id_num, obj):
        return self.m_table.update(obj, doc_ids=[id_num])

    def delete_match(self, id_num):
        return self.m_table.remove(doc_ids=[id_num])


"""
Un match unique doit être stocké sous la forme d'un tuple contenant deux listes,
chacune contenant deux éléments : une référence à une instance de joueur et un score.
Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
"""
