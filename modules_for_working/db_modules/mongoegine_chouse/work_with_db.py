from fastapi import HTTPException

from modules_for_working.db_modules.mongoegine_chouse.db_connect import DBConnect
from modules_for_working.db_modules.mongoegine_chouse.models_mongo_engine.users import Users
import json


class DataFlowWithDB(object):

    def __init__(self):
        self.connect = DBConnect().con

    @staticmethod
    def update_user_data(_id, user_data):
        Users.objects(id=_id).update(user_data=user_data)

    @staticmethod
    def get_user_data():
        return [json.loads(i.to_json()) for i in Users.objects.only("username", "user_data")]

    @staticmethod
    def get_username(username):
        try:
            user = Users.objects(username=username)[0]
            return {"username": user.username, "password": user.password, "role": user.role}
        except Exception:
            return None

    @staticmethod
    def add_new_user(user):
        new_user = Users(username=user["username"], password=user["password"], role=user["role"],
                         user_data=user["user_data"])
        new_user.save()

    @staticmethod
    def delete_cur_user(_id, username):
        user = Users.objects(id=_id)[0]
        if user.username == username:
            raise HTTPException(status_code=400, detail="You can't delete yourself")
        else:
            Users.objects(id=_id).delete()
