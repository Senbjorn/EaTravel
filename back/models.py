from datetime import datetime
from back import db
from mongoengine import fields

class UserModel(db.Document):
    age = fields.IntField(required=True)
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True, unique=True)
    created_at = fields.DateField(default=datetime.now)