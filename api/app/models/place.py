from app.models.base import BaseModel
from app.models.city import City
from app.models.user import User
import peewee

class Place(BaseModel):
    city = peewee.ForeignKeyField(City, related_name="places", on_delete="cascade")
    owner = peewee.ForeignKeyField(User, related_name="places", on_delete="cascade")
    name = peewee.FixedCharField(max_length=128, unique=True)
    description = peewee.TextField()
    number_rooms = peewee.IntegerField(default=0)
    number_bathrooms = peewee.IntegerField(default=0)
    max_guest = peewee.IntegerField(default=0)
    price_by_night = peewee.IntegerField(default=0)
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()

    def to_dict(self):
        data = BaseModel.to_dict(self)
        data["name"] = self.name
        data["owner_id"] = self.owner.id
        data["city_id"] = self.city.id
        data["description"] = self.description
        data["number_rooms"] = self.number_rooms
        data["number_bathrooms"] = self.number_bathrooms
        data["max_guest"] = self.max_guest
        data["price_by_night"] = self.price_by_night
        data["latitude"] = self.latitude
        data["longitude"] = self.longitude
        return data
