import json

from pymongo import MongoClient


class InsertDocuments:
    def __init__(self, uri, database, collection):
        self.uri = uri
        self.client = MongoClient(uri)
        self.database = database
        self.collection = collection

    def __del__(self):
        self.client.close()

    def drop_database(self, db_name):
        self.client.drop_database(db_name)

    def drop_collection(self, db_name, collection_name):
        self.client[db_name].drop_collection(collection_name)

    def insert_document(self, db_name, collection_name, document):
        db = self.client[db_name]
        collection = db[collection_name]
        return collection.insert_one(document).inserted_id

    def insert_documents(self, db_name, collection_name, documents):
        db = self.client[db_name]
        collection = db[collection_name]
        return collection.insert_many(documents).inserted_ids

    def insert_json_file(self, db_name, collection_name, file_path):
        db = self.client[db_name]
        collection = db[collection_name]

        with open(file_path, encoding="utf-8") as file:
            file = json.load(file)

        return collection.insert_many(file)


if __name__ == "__main__":
    uri = "mongodb://localhost:27017"

    database = "Alura_Series"
    collection = "series"

    # Instancia a classe
    insert_documents = InsertDocuments(uri, database, collection)

    # Se o banco de dados existir, ele será descartado
    insert_documents.drop_database(database)

    # Se a coleção existir, ela será descartada
    insert_documents.drop_collection(database, collection)

    # Insere um documento
    document = {
        "titulo": "Star Wars",
        "ano": 1977,
        "diretor": "George Lucas"
    }
    insert_id = insert_documents.insert_document(database, collection, document)
    print(insert_id)

    # Insere vários documentos
    documents = [
        {
            "titulo": "Harry Potter",
            "ano": 2001,
            "diretor": "Chris Columbus"
        },
        {
            "titulo": "Avengers",
            "ano": 2012,
            "diretor": "Joss Whedon"
        },
        {
            "titulo": "Matrix",
            "ano": 1999,
            "diretor": "Wachowski"
        }
    ]
    insert_ids = insert_documents.insert_documents(database, collection, documents)
    print(insert_ids)

    # Insere um documento a partir de um arquivo
    file_path = "data/Base de dados.json"
    insert_file = insert_documents.insert_json_file(database, collection, file_path)
    print(insert_file)

    # Exibe os documentos inseridos
    for document in insert_documents.client[database][collection].find():
        print(document)

    # Comentar a linha abaixo para não excluir o banco de dados
    insert_documents.drop_database(database)
