from helpers import get_vector
from time import sleep
import requests
from requests.adapters import HTTPAdapter


class VectorContainer:
    def __init__(self):
        self._config = self.config_setting()
        self._session = requests.Session()
        self._url = 'http://' + self._config['host'] + ':' + self._config['port'] + self._config['prefix']

    @staticmethod
    def config_setting():
        config = get_vector('AI')
        return config

    def get_vector_data(self, data):
        params = {'sentence': data}
        try:
            response = self._session.get(self._url, params=params).json()
            response = response['vector'][0]
        except:
            self._session = requests.Session()
            response = -1

        return response

    @staticmethod
    def use_cosine_similarity_scoring():
        return 'cosineSimilarity(params.query_vector, \'vector\') + 1.0 + _score'

    @staticmethod
    def use_cosine_similarity_scoring_weight(weight):
        return '(cosineSimilarity(params.query_vector, \'vector\') + 1.0) * ' + str(weight) + '* _score'
