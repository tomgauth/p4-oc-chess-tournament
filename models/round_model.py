from tinydb import Query, where
from jsonmodels import models, fields, validators
from jsonmodels.errors import ValidationError
import uuid


class Round(models.Base):
    matches = fields.ListField(default=[])
    id_key = fields.StringField(required=True,
                                validators=validators.Length(
                                    minimum_value=36, maximum_value=36))
    round_num = fields.IntField(default=1)


class RoundHandler():
    def __init__(self, rounds_table):
        self.r_table = rounds_table

    def to_obj(self, round_doc):
        play_round = Round(
            matches=[],
            id_key=round_doc.get('id_key'),
            round_num=round_doc.get('round_num', 1))

        matches_list = round_doc.get('matches', [])
        # TODO refacto? looks fishy
        play_round.matches = play_round.matches.append(matches_list)
        return play_round

    def save_to_db(self, play_round):
        # check if there is already a play_round with this id
        try:
            # self.r_table.contains(Query().id_key == play_round.id_key)
            self.r_table.update(play_round.to_struct(),
                                Query().id_key == play_round.id_key)
        except ValidationError:
            play_round.id_key = str(uuid.uuid4())
            self.r_table.insert(play_round.to_struct())
        return play_round

    def destroy(self, play_round_id):
        self.r_table.remove(where('id_key') == play_round_id)

    def all_play_rounds(self):
        play_rounds_as_obj = []
        all_play_rounds = self.r_table.all()
        for play_round in all_play_rounds:
            obj = self.to_obj(play_round)
            play_rounds_as_obj.append(obj)
        return play_rounds_as_obj

    def search(self, **kwargs):
        result = self.r_table.search(Query().fragment(kwargs))
        if len(result) == 1:
            output = self.to_obj(result[0])
        else:  # return a list of objects
            output = []
            for r in result:
                output.append(self.to_obj(r))
        print(output)
        print(type(output))
        return output

    def upsert(self, play_round):
        self.r_table.upsert(play_round.to_struct(),
                            Query().id_key == play_round.id_key)
