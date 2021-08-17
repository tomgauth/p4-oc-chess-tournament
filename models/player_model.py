# This is the player model
from tinydb import TinyDB, Query
db = TinyDB('db.json')


class Player:
    def __init__(self, last_name='', first_name='', birth_date='',
                 sex='', ranking=0):
        self.p_table = db.table('players')
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.ranking = ranking
        self.id = ''

    def create_player(self):
        player_id = self.p_table.insert(
            {"last_name": self.last_name,
             "first_name": self.first_name,
             "birth_date": self.birth_date,
             "sex": self.sex,
             "ranking": self.ranking
             })
        return self.p_table.update({'id': player_id}, doc_ids=[player_id])[0]

    def save_player(self):
        if self.id == '':
            result = self.create_player()
        else:
            result = self.p_table.update(
                {"last_name": self.last_name,
                 "first_name": self.first_name,
                 "birth_date": self.birth_date,
                 "sex": self.sex,
                 "ranking": self.ranking,
                 "id": self.id
                 }, doc_ids=[self.id])[0]
        return result

    def current_score(self, tournament):
        score = 0
        for round_ in tournament.rounds:
            for match in round_.matches:
                if match.p1_score != '':
                    if match.p1_id == self.id:
                        score += match.p1_score
                    elif match.p2_id == self.id:
                        score += match.p2_score
        return score

    def played_against(self, tournament):
        previous_opponents = []
        for round_ in tournament.rounds:
            for match in round_.matches:
                if match.p1_id == self.id:
                    player2 = Player.get_player_from_id(match.p2_id)
                    previous_opponents.append(player2)
                elif match.p2_id == self.id:
                    player1 = Player.get_player_from_id(match.p1_id)
                    previous_opponents.append(player1)
        return previous_opponents

    @staticmethod
    def get_player_from_id(id_num):
        player = Player()
        player_data = player.p_table.get(doc_id=int(id_num))
        player.last_name = player_data["last_name"]
        player.first_name = player_data["first_name"]
        player.birth_date = player_data["birth_date"]
        player.sex = player_data["sex"]
        player.ranking = player_data["ranking"]
        player.id = id_num

        return player

    # this function is deprecated

    def get_player_id(self):
        # use first_name, last_name, birth_date to find the player in the db
        query = Query()
        found_player = self.p_table.get(
            query.fragment({
                'first_name': self.first_name,
                'last_name': self.last_name,
                'birth_date': self.birth_date}))

        return found_player.doc_id

    def read_player(self, id_num):
        """ find a player by id """
        """ check how to get object by id in tinydb """
        return self.p_table.get(doc_id=id_num)

    def read_players(self):
        """ returns all players """
        return self.p_table.all()

    def update_player(self, id_num, obj):
        return self.p_table.update(obj, doc_ids=[id_num])

    def delete_player(self, id_num):
        return self.p_table.remove(doc_ids=[id_num])
