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
    rounds = fields.ListField(default=[], nullable=True)
    players = fields.ListField(default=[], nullable=True)
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
        tournament = Tournament(
            name=tournament_doc.get('name'),
            location=tournament_doc.get('location', None),
            date_start=tournament_doc.get('date_start', None),
            date_end=tournament_doc.get('date_end', None),
            num_of_rounds=tournament_doc.get('num_of_rounds', None),
            time_control=tournament_doc.get('time_control', None),
            id_key=tournament_doc.get('id_key'),
            players=[],
            rounds=[])

        players_list = tournament_doc.get('players', [])
        tournament.players = tournament.players.extend(players_list)
        rounds_list = tournament_doc.get('rounds', [])
        tournament.rounds = tournament.rounds.extend(rounds_list)

        return tournament

    def save_to_db(self, tournament):
        # check if there is already a tournament with this id
        try:
            # self.t_table.contains(Query().id_key == tournament.id_key)
            self.t_table.update(tournament.to_struct(),
                                Query().id_key == tournament.id_key)
        except ValidationError:
            tournament.id_key = str(uuid.uuid4())
            self.t_table.insert(tournament.to_struct())
        return tournament

    def destroy(self, tournament_id):
        self.t_table.remove(where('id_key') == tournament_id)

    def all_tournaments(self):
        tournaments_as_obj = []
        all_tournaments = self.t_table.all()
        for tournament in all_tournaments:
            obj = self.to_obj(tournament)
            tournaments_as_obj.append(obj)
        return tournaments_as_obj

    def search(self, **kwargs):
        result = self.t_table.search(Query().fragment(kwargs))
        if len(result) == 1:
            output = self.to_obj(result[0])
        else:  # return a list of objects
            output = []
            for r in result:
                output.append(self.to_obj(r))
        print(output)
        print(type(output))
        return output

    def upsert(self, tournament):
        self.t_table.upsert(tournament.to_struct(),
                            Query().id_key == tournament.id_key)
