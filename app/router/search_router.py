from fastapi import APIRouter
from datetime import date
from app.search.elastic_search import ElasticSearch
from ..search.make_query import *
from data_processor import *
from app.models.response_model import ResponseModel, SortModeResponseModel

search_router = APIRouter(
    prefix="/search"
)

es = ElasticSearch('news-search')


@search_router.get(path="/match_all", response_model=ResponseModel)
async def search_all():
    match_all_query = get_match_all_query()
    search_all_object = es.search(match_all_query)
    response_model = data_list_to_match_model(search_all_object)
    return response_model


@search_router.get(path="/match/{terms}", response_model=ResponseModel)
async def search_with_or(terms: str):
    match_query = get_match_query_basic(terms, 'korean_analyzer')
    search_object = es.search(match_query)
    response_model = data_list_to_match_model(search_object)
    return response_model


@search_router.get(path="/match/zeroterms/{terms}", response_model=ResponseModel)
async def search_result_zero_terms(terms: str):
    match_query = get_match_query_zero_terms(terms, 'korean_analyzer', True)
    search_zero_object = es.search(match_query)
    response_model = data_list_to_match_model(search_zero_object)
    return response_model


@search_router.get(path="/match/and/{terms}", response_model=ResponseModel)
async def search_with_and(terms: str):
    match_query = get_match_query_basic(terms, 'korean_analyzer', True)
    search_and_object = es.search(match_query)
    response_model = data_list_to_match_model(search_and_object)
    return response_model


@search_router.get(path="/match/{terms}/analyzers/{analyzer}", response_model=ResponseModel)
async def search_with_analyzer(terms: str, analyzer: str):
    match_query = get_match_query_basic(terms, analyzer)
    search_data_object = es.search(match_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/match/and/{terms}/analyzers/{analyzer}", response_model=ResponseModel)
async def search_with_and_analyzer(terms: str, analyzer: str):
    match_query = get_match_query_basic(terms, analyzer, True)
    search_data_object = es.search(match_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/match/email/{email}", response_model=ResponseModel)
async def search_with_email(email: str):
    match_email_query = get_email_query(email)
    search_data_object = es.search(match_email_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/match/date/{day}", response_model=ResponseModel)
async def search_with_date(day: date):
    match_date_query = get_date_query(day)
    search_data_object = es.search(match_date_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/phrase/{terms}/{slop}", response_model=ResponseModel)
async def search_with_phrase(terms: str, slop: int):
    match_phrase_query = get_match_phrase_basic(terms, slop)
    search_data_object = es.search(match_phrase_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/multi/{terms}", response_model=ResponseModel)
async def multi_search(terms: str):
    multi_match_query = get_multi_match_query(terms)
    search_data_object = es.search(multi_match_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/bool/must/{must_first_terms}/must/{must_second_terms}")
async def bool_must_search(must_first_terms: str, must_second_terms: str):
    bool_search_query = get_bool_must_match_query(must_first_terms, must_second_terms)
    search_data_object = es.search(bool_search_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/bool/{must_terms}/{should_terms}", response_model=ResponseModel)
async def bool_search(must_terms: str, should_terms: str):
    bool_search_query = get_bool_match_query(must_terms, should_terms)
    search_data_object = es.search(bool_search_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/bool/{must_terms}/{should_terms}/filters/{filter_terms}", response_model=ResponseModel)
async def bool_filter_search(must_terms: str, should_terms: str, filter_terms: str):
    bool_filter_search_query = get_bool_match_query(must_terms, should_terms, filter_terms)
    search_data_object = es.search(bool_filter_search_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/multi/terms/{terms}/fields/{fields}", response_model=ResponseModel)
async def multi_boost_search(boost: str, terms: str, fields: str):
    multi_boost_search_query = get_multi_boost_query(boost, terms, fields)
    search_data_object = es.search(multi_boost_search_query)
    response_model = data_list_to_match_model(search_data_object)
    return response_model


@search_router.get(path="/highlight/terms/{terms}", response_model=HighlightResponseModel)
async def search_with_highlight(terms: str):
    highlight_search_query = get_highlight_query(terms)
    search_highlight_object = es.search(highlight_search_query)
    response_model = data_list_to_match_highlight_model(search_highlight_object)
    return response_model


@search_router.get(path="/highlight/terms/{terms}/fragment_size/{size}", response_model=HighlightResponseModel)
async def search_with_highlight_control_fragments(terms: str, size: int):
    highlight_search_query = get_highlight_query_with_size(terms, size)
    search_highlight_object = es.search(highlight_search_query)
    response_model = data_list_to_match_highlight_model(search_highlight_object)
    return response_model


@search_router.get(path="/highlight/terms/{terms}/max_fragment/{size}", response_model=HighlightResponseModel)
async def search_with_highlight_control_max_fragements(terms: str, size: int):
    highlight_search_query = get_highlight_query_with_max_size(terms, size)
    search_highlight_object = es.search(highlight_search_query)
    response_model = data_list_to_match_highlight_model(search_highlight_object)
    return response_model


@search_router.get(path="/highlight/terms/{terms}/tags/{tag}", response_model=HighlightResponseModel)
async def search_with_highlight_and_tags(terms: str, tag: str):
    highlight_search_query = get_highlight_query_with_tag(terms, tag)
    search_highlight_object = es.search(highlight_search_query)
    response_model = data_list_to_match_highlight_model(search_highlight_object)
    return response_model


@search_router.get(path="/sort/terms/{terms}/options/{option}", response_model=SortModeResponseModel)
async def search_with_sort_mode_option(terms: str, option: str):
    sort_option_query = get_search_with_sort_option(terms, option)
    search_sort_object = es.search(sort_option_query, 'my-sample')
    response_model = data_to_sort_model(search_sort_object)
    return response_model
