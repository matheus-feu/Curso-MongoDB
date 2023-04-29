from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

"""
pip install pymongo

Use o PyMongo para aplicativos Python síncronos.
PyMongo, uma distribuição do Python que contém ferramentas para trabalhar com o MongoDB e é a maneira recomendada 
de trabalhar com o MongoDB a partir do Python.
"""


def connect_mongo(uri):
    try:
        client = MongoClient(uri, server_api=ServerApi(version="1"))
        client.admin.command("ping")
        return True
    except errors.ConnectionFailure as e:
        raise e


uri = "mongodb://localhost:27017"
if connect_mongo(uri):
    print("Connected to MongoDB")
else:
    print("Could not connect to MongoDB")
