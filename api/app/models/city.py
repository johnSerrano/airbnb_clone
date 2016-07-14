from app.models.base import BaseModel
from app.models.state import State
import peewee

class City(BaseModel):
    name = peewee.FixedCharField(max_length=128, unique=True)
    state = peewee.ForeignKeyField(State, related_name="cities", on_delete="cascade")

    def to_hash(self):
        data = BaseModel.to_hash(self)
        data["name"] = self.name
        data["state_id"] = self.state.id
        return data
