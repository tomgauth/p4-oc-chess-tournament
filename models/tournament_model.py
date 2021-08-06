# This is the tournament model


class Tournament:
    def __init__(self, t_table, name='', location='', date_start='',
                 date_end='', num_of_rounds=4, rounds=[], players=[],
                 time_control='', description=''):
        self.t_table = t_table
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
            {'name': self.name,
             'location': self.location,
             'date_start': self.date_start,
             'date_end': self.date_end,
             'num_of_rounds': self.num_of_rounds,
             'rounds': self.rounds,
             'players': self.players,
             'time_control': self.time_control,
             'description': self.description
             })

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
