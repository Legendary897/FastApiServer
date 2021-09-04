from mongoengine import *
from modules_for_working.models.model_for_mongo import UserData


class UserData(EmbeddedDocument):
    name = StringField(required=True, max_length=50)
    surname = StringField(required=True, max_length=50)
    old = IntField(required=True, max_length=50)


class Users(Document):
    username = StringField(required=True, max_length=200)
    password = StringField(required=True)
    role = IntField(required=True)
    user_data = EmbeddedDocumentField(UserData)
