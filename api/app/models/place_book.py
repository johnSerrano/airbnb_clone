from app.models.place import Place
from app.models.user import User
from app.models.base import BaseModel
import peewee

class PlaceBook(BaseModel):
    place = peewee.ForeignKeyField(Place, on_delete="cascade")
    user = peewee.ForeignKeyField(User, related_name="places_booked", on_delete="cascade")
    is_validated = peewee.BooleanField(default=False)
    date_start = peewee.DateTimeField()
    number_nights = peewee.IntegerField(default=1)

    def to_hash(self):
        data = BaseModel.to_hash(self)
        data["place_id"] = self.place.id
        data["user_id"] = self.user.id
        data["is_validated"] = self.is_validated
        data["date_start"] = self.date_start
        data["number_nights"] = self.number_nights
        return data
