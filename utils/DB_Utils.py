import pymongo
from bson import ObjectId
from pymongo import mongo_client

from utils.CommonUtils import CommonUtils


class DB_Utils:

    @staticmethod
    def db_connect():
        config = CommonUtils.read_prop_file()
        client = pymongo.MongoClient(config.get('details', 'dbUrl'))
        db = client[config.get('details', 'db')]
        information = db.credentials
        # d = information.find_one( {"_id": ObjectId("507f191e810c19729de860ea")},{'_id' : 0})
        # print(d["ui_email"])
        # print(d["ui_password"])
        # for data in d.values():
        #     print(data)
        # print(d)
        return information


# info = DB_Utils.db_connect()

