from app.models.place import Place
from app.models.amenity import Amenity
from app.models.base import db
import peewee

class PlaceAmenities(peewee.Model):
    place = peewee.ForeignKeyField(Place, on_delete="cascade")
    amenity = peewee.ForeignKeyField(Amenity, on_delete="cascade")

    class Meta:
        database = db
