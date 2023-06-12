import threading
from typing import Dict

from pymongo import MongoClient
from pymongo.results import InsertOneResult


class Database:
    """
        Contains a singleton instance of mongo database to interact with
    """
    _instance = None
    _database = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                # Another thread could have created the instance
                # before we acquired the lock. So check that the
                # instance is still nonexistent.
                if not cls._instance:
                    cls._instance = super().__new__(cls)

                    if "host" in kwargs:
                        host = kwargs["host"]
                    else:
                        host = "localhost"

                    if "port" in kwargs:
                        port = kwargs["port"]
                    else:
                        port = 27017

                    if "database" in kwargs:
                        database = kwargs["database"]
                    else:
                        database = "bienestar_emocional"

                    cls._database = MongoClient(host, port).get_database(database)
        return cls._instance

    @staticmethod
    def insert_user_data(data: Dict) -> InsertOneResult:
        """
        Insert data into user_data collection
        :param data: data to insert
        :return: InsertOneResult of the execution
        """
        collection = Database._database.get_collection('user_data')
        return collection.insert_one(data)

    @staticmethod
    def insert_daily_questionnaires(data: Dict) -> InsertOneResult:
        """
        Insert data into daily_questionnaires collection
        :param data: data to insert
        :return: InsertOneResult of the execution
        """
        collection = Database._database.get_collection('daily_questionnaires')
        return collection.insert_one(data)
