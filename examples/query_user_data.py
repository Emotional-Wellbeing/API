from pprint import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.get_database('bienestar_emocional')
collection = db.get_collection('user_data')

for item in collection.find():
    pprint(item)

