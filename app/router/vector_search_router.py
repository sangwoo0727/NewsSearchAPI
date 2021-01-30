from fastapi import APIRouter
from app.search.elastic_search import ElasticSearch
from app.search.make_query import *
from data_processor import *

vector_search_router = APIRouter(
    prefix="/vector"
)

es = ElasticSearch('news-search')
vector_container = VectorContainer()


@vector_search_router.get(path="/match_all", response_model=ResponseModel)
async def match_all():
    query = get_match_all_query()
    search_all_object = es.search(query)
    response_model = data_list_to_match_model(search_all_object)
    return response_model


@vector_search_router.get(path="/match/{terms}", response_model=ResponseModel)
async def match(terms: str):
    query_vector = vector_container.get_vector_data(terms)
    match_query = get_vector_match_query(terms, query_vector)
    search_match_object = es.search(match_query)
    response_model = data_list_to_match_model(search_match_object)
    return response_model


@vector_search_router.get(path="/match/{terms}/weight/{weight}", response_model=ResponseModel)
async def match_weight(terms: str, weight: int):
    query_vector = vector_container.get_vector_data(terms)
    match_query = get_vector_weight_match_query(terms, weight, query_vector)
    search_match_object = es.search(match_query)
    response_model = data_list_to_match_model(search_match_object)
    return response_model
