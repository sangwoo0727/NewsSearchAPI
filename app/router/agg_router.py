from fastapi import APIRouter
from app.search.elastic_search import ElasticSearch
from app.models.response_model import *
from app.search.make_query import *
from data_processor import *

agg_router = APIRouter(
    prefix="/agg"
)

es = ElasticSearch('news-search')


@agg_router.get(path="/basic/fields/{fields}", response_model=AggregationResponseModel)
async def agg_basic(fields: str):
    agg_query = get_agg_query_basic(fields)
    agg_result = es.search(agg_query)
    response_model = data_obj_to_agg_model(agg_result)
    return response_model
