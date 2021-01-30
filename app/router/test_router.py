from fastapi import APIRouter
from ..search.make_query import *
from ..search.elastic_search import ElasticSearch
from app.models.test_response_model import TestResponseModel
from data_processor import data_to_test_model

test_router = APIRouter(
    prefix="/test"
)

es = ElasticSearch('news-search')


@test_router.get(path="/analyzers/{analyzer}/text/{text}", response_model=TestResponseModel)
async def search_test(analyzer: str, text: str):
    test_query = get_test_query(analyzer, text)
    search_test_obj = es.search(test_query)
    response_model = data_to_test_model(search_test_obj)
    return response_model

