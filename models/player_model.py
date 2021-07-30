# This is the player model
from tinydb import Query, where
from jsonmodels import models, fields, validators
from jsonmodels.errors import ValidationError
import uuid


class Player(models.Base):
    last_name = fields.StringField(required=False)
    first_name = fields.StringField(required=True)
    sex = fields.StringField(default='N/A',
                             validators=validators.Enum('M', 'F', 'O', 'N/A'))
    ranking = fields.IntField(default=None)
    id_key = fields.StringField(required=True,
                                validators=validators.Length(
                                    minimum_value=36, maximum_value=36))


class PlayerHandler:
    def __init__(self, players_table):
        self.p_table = players_table

    def to_obj(self, player_doc):
        return Player(last_name=player_doc.get('last_name', None),
                      first_name=player_doc.get('first_name', None),
                      sex=player_doc.get('sex', "N/A"),
                      ranking=player_doc.get('ranking', None),
                      id_key=player_doc.get('id_key')
                      )

    def save_to_db(self, player):
        # check if there is already a player with this id
        try:
            # self.p_table.contains(Query().id_key == player.id_key)
            self.p_table.update(player.to_struct(),
                                Query().id_key == player.id_key)
        except ValidationError:
            print('PLAYERHANDLER ValidationError')
            player.id_key = str(uuid.uuid4())
            print('PLAYERHANDLER - ASSIGNED ID',player.id_key)
            self.p_table.insert(player.to_struct())
        print('PLAYERHANDLER ', player.id_key)
        return player

    def destroy(self, player_id):
        self.p_table.remove(where('id_key') == player_id)

    def all_players(self):
        return self.p_table.all()

    # returns any Player with corresponding keywords arguments
    # ex: search(first_name='John', rank=32)
    # => [{'first_name': 'John', 'last_name': 'G', 'ranking': 32, 'sex': 'M'}]
    def search(self, **kwargs):
        result = self.p_table.search(Query().fragment(kwargs))
        if len(result) == 1:
            result = result[0]
        return self.to_obj(result)

    def upsert(self, player):
        self.p_table.upsert(player.to_struct(),
                            Query().id_key == player.id_key)
