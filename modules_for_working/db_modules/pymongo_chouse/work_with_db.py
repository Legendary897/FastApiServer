from fastapi import HTTPException

from modules_for_working.db_modules.pymongo_chouse.db_connect import DBConnect as db


class DataFlowWithDB(object):

    def __init__(self):
        self.db = db()

    def update_user_data(self, _id, user_data):
        self.db.work_collection.update_one({"_id": _id}, {"$set": {"user_data": user_data}})

    def get_user_data(self):
        list_users = []
        for i in self.db.work_collection.find({}, {"username": 1, "user_data": 1}):
            i["_id"] = str(i["_id"])
            list_users.append(i)
        return {"all_data": list_users}

    def get_username(self, username):
        return self.db.work_collection.find_one({"username": {"$in": [username]}},
                                                {"username": 1, "password": 1, "role": 1})

    def add_new_user(self, user):
        self.db.work_collection.insert_one(user)

    def delete_cur_user(self, _id, username):
        user = self.db.work_collection.find_one({"_id": _id}, {"username": 1})
        if user["username"] == username:
            raise HTTPException(status_code=400, detail="You can't delete yourself")
        else:
            self.db.work_collection.delete_one({"_id": _id})
