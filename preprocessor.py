import pymysql
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from helpers import get_db, get_vector
from app.vector.vector_container import *


class DbController:
    def __init__(self):
        self.cursor = self.connect()

    def connect_close(self):
        self.cursor.close()

    def connect(self):
        config = get_db('DB')
        host = config['host']
        port = int(config['port'])
        id = config['id']
        password = config['password']
        db = config['database']
        conn = pymysql.connect(host=host, user=id, password=password, database=db, port=port, charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return cursor

    def get_all(self):
        sql = "SELECT * FROM news"
        self.cursor.execute(sql)
        list = self.cursor.fetchall()
        return list


def bulk_insert(data_list):
    es = Elasticsearch()
    vc = VectorContainer()
    documents = []
    for data in data_list:
        vector = vc.get_vector_data(data['contents'])
        if vector == -1:
            continue
        document = {
            "_index": "news-search",
            "_id": data['id'],
            "_source": {
                "id": data['id'],
                "date": data['date'],
                "category": data['category'],
                "headline": data['headline'],
                "contents": data['contents'],
                "vector": vector
            }
        }
        documents.append(document)
    helpers.bulk(es, documents)


def main():
    db = DbController()
    data_list = db.get_all()
    db.connect_close()
    bulk_insert(data_list)


main()
