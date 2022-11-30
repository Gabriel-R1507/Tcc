from pymongo import MongoClient
from decouple import config

def get_database():

    MONGODB_URL = config("MONGODB_URL")
    client = MongoClient(MONGODB_URL)
    return client