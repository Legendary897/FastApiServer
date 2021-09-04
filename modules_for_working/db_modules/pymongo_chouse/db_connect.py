from pymongo import MongoClient
from modules_for_working.db_modules.pymongo_chouse.settings_db import settings


class DBConnect(object):

    def __init__(self):
        self.client = MongoClient(settings["host"], settings["port"])
        self.db = self.client.test
        self.work_collection = self.db.users
