import config
import peewee
import datetime
from app.models import db

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
    updated_at = peewee.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        peewee.Model.save(self, args, kwargs)

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    class Meta:
        database = db
        order_by = ("id",)



def test_import():
    return config.DATABASE
