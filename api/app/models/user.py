from app.models.base import BaseModel
import peewee
import hashlib

class User(BaseModel):
    email = peewee.FixedCharField(max_length=128, unique=True)
    password = peewee.FixedCharField(max_length=128)
    first_name = peewee.FixedCharField(max_length=128)
    last_name = peewee.FixedCharField(max_length=128)
    is_admin = peewee.BooleanField(default=False)

    def to_hash(self):
        data = BaseModel.to_hash(self)
        data["email"] = self.email
        data["first_name"] = self.first_name
        data["last_name"] = self.last_name
        data["is_admin"] = self.is_admin
        return data

    def set_password(self, clear_password):
        m = hashlib.md5()
        m.update(clear_password)
        hashedpass = m.hexdigest()
        self.password = hashedpass
