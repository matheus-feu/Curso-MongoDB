from pymongo import MongoClient


class QueryDocuments:
    def __init__(self, uri, database, collection):
        self.uri = uri
        self.client = MongoClient(uri)
        self.database = database
        self.collection = collection

    def query_document(self, db_name, collection_name, query):
        db = self.client[db_name]
        collection = db[collection_name]
        return collection.find_one(query)


if __name__ == "__main__":
    uri = "mongodb://localhost:27017"

    database = "Alura_Series"
    collection = "series"

    # Instancia a classe
    query_documents = QueryDocuments(uri, database, collection)

    # Consulta um documento
    query = {"titulo": "Star Wars"}

    document = query_documents.query_document(database, collection, query)
    print(document)
