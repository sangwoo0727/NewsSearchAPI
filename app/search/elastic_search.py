from elasticsearch import Elasticsearch
from helpers import get_host


class ElasticSearch(Elasticsearch):
    def __init__(self, index, **kwargs):
        host = get_host('ES')
        self._index = index
        super().__init__(host, **kwargs)

    def search(self, body, index=None):
        if index is None:
            index = self._index
        return super().search(body=body, index=index)
