from pprint import pprint
from pymongo import MongoClient

from src.database import Database

client = MongoClient('localhost', 27017)
db = client.get_database('bienestar_emocional')
collection = db.get_collection('daily_questionnaires')

database = Database()

query = database.get_daily_questionnaires_average(1686866400000, 1686952799000)

print(query)
