import peewee
from app.models.base import BaseModel

class Amenity(BaseModel):
    name = peewee.FixedCharField(max_length=128, unique=True)

    def to_dict(self):
        data = BaseModel.to_dict(self)
        data["name"] = self.name
        return data
