from mongoengine import connect
from modules_for_working.db_modules.mongoegine_chouse.settings_db import settings


class DBConnect(object):

    def __init__(self):
        self.con = connect(settings["db"], host=settings["host"], port=settings["port"])
