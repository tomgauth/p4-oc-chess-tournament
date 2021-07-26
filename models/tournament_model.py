# This is the tournament model
from tinydb import Query, where
from jsonmodels import models, fields, validators
from jsonmodels.errors import ValidationError
import uuid


class Tournament(models.Base):
    name = fields.StringField(required=True)
    location = fields.StringField(required=False)
    date_start = fields.DateField(str_format='%d-%m-%Y',
                                  required=False)
    date_end = fields.DateField(str_format='%d-%m-%Y',
                                required=False, default=None)
    num_of_rounds = fields.IntField(required=False, default=4)
    rounds = fields.ListField(required=False, default=[])
    players = fields.ListField(required=False, default=[])
    time_control = fields.StringField(default=None,
                                      validators=validators.Enum(None,
                                                                 'bullet',
                                                                 'blitz',
                                                                 'rapid'))
    description = fields.StringField(required=False)
    id_key = fields.StringField(required=True,
                                validators=validators.Length(
                                    minimum_value=36, maximum_value=36))


class TournamentHandler:
    def __init__(self, tournaments_table):
        self.t_table = tournaments_table

    def to_obj(self, tournament_doc):
        return Tournament(
            name=tournament_doc.get('name'),
            location=tournament_doc.get('location', None),
            date_start=tournament_doc.get('date_start', None),
            date_end=tournament_doc.get('date_end', None),
            num_of_rounds=tournament_doc.get('num_of_rounds', None),
            rounds=tournament_doc.get('rounds', []),
            players=tournament_doc.get('players', []),
            time_control=tournament_doc.get('time_control', None))

    def save_to_db(self, tournament):
        # check if there is already a tournament with this id
        try:
            # self.p_table.contains(Query().id_key == tournament.id_key)
            self.p_table.update(tournament.to_struct(),
                                Query().id_key == tournament.id_key)
        except ValidationError:
            tournament.id_key = str(uuid.uuid4())
            self.p_table.insert(tournament.to_struct())

    def destroy(self, tournament_id):
        self.p_table.remove(where('id_key') == tournament_id)

    def all_tournaments(self):
        return self.p_table.all()

    def search(self, **kwargs):
        result = self.p_table.search(Query().fragment(kwargs))
        if len(result) == 1:
            result = result[0]
        return self.to_obj(result)

    def upsert(self, tournament):
        self.p_table.upsert(tournament.to_struct(),
                            Query().id_key == tournament.id_key)
