import peewee
from app.models.user import User
from app.models.state import State
from app.models.city import City
from app.models.place import Place
from app.models.place_book import PlaceBook 
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities


def create_database():
    try:
         User.create_table()
    except peewee.OperationalError:
        pass

    try:
         State.create_table()
    except peewee.OperationalError:
        pass

    try:
         City.create_table()
    except peewee.OperationalError:
        pass

    try:
         Place.create_table()
    except peewee.OperationalError:
        pass

    try:
         PlaceBook.create_table()
    except peewee.OperationalError:
        pass

    try:
         Amenity.create_table()
    except peewee.OperationalError:
        pass

    try:
         PlaceAmenities.create_table()
    except peewee.OperationalError:
        pass

if __name__ == "__main__":
    create_database()
