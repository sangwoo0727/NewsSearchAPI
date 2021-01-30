from app.models.match_data_model import MatchDataModel
from app.models.response_model import ResponseModel, HighlightModel, HighlightResponseModel, AggregationResponseModel
from app.models.token_model import TokenModel
from app.models.test_response_model import TestResponseModel
from app.models.response_model import SortModeResponseModel, SortModeModel


def data_list_to_match_model(obj):
    model_list = []
    total = obj['hits']['total']['value']
    max_score = 0 if obj['hits']['max_score'] is None else obj['hits']['max_score']
    data_list = obj['hits']['hits']
    for data in data_list:
        score = data['_score']
        id = data['_source']['id']
        date = data['_source']['date']
        category = data['_source']['category']
        headline = data['_source']['headline']
        contents = data['_source']['contents']
        match_data_model = MatchDataModel(score=score, id=id, date=date, category=category, headline=headline,
                                          contents=contents)
        model_list.append(match_data_model)
    response_model = ResponseModel(total=total, max_score=max_score, data=model_list)
    return response_model


def data_to_test_model(obj):
    token_model_list = []
    data_list = obj['tokens']
    for data in data_list:
        token = data['token']
        start_offset = data['start_offset']
        end_offset = data['end_offset']
        position = data['position']
        token_model = TokenModel(token=token, start_offset=start_offset, end_offset=end_offset, position=position)
        token_model_list.append(token_model)
    total = len(token_model_list)
    test_response_model = TestResponseModel(total=total, tokens=token_model_list)
    return test_response_model


def data_list_to_match_highlight_model(obj):
    highlight_model_list = []
    data_list = obj['hits']['hits']
    total = 0 if obj['hits']['total']['value'] is None else obj['hits']['total']['value']
    max_score = 0 if obj['hits']['max_score'] is None else obj['hits']['max_score']
    for model in data_list:
        source = model['_source']
        score = model['_score']
        id = source['id']
        date = source['date']
        category = source['category']
        headline = source['headline']
        contents = source['contents']
        highlight = model['highlight']['contents']
        highlight_model = HighlightModel(id=id, score=score, date=date, category=category, headline=headline,
                                         contents=contents, highlight=highlight)
        highlight_model_list.append(highlight_model)
    response_model = HighlightResponseModel(total=total, max_score=max_score, data=highlight_model_list)
    return response_model


def data_to_sort_model(obj):
    sort_model_list = []
    data_list = obj['hits']['hits']
    for model in data_list:
        product = model['_source']['product']
        price = model['_source']['price']
        sort = model['sort']
        sort_model = SortModeModel(product=product, price=price, sort=sort)
        sort_model_list.append(sort_model)
    response_model = SortModeResponseModel(data=sort_model_list)
    return response_model


def data_obj_to_agg_model(obj):
    doc_count_error_upper_bound = obj['aggregations']['my-agg']['doc_count_error_upper_bound']
    sum_other_doc_count = obj['aggregations']['my-agg']['sum_other_doc_count']
    buckets = obj['aggregations']['my-agg']['buckets']
    response_model = AggregationResponseModel(doc_count_error_upper_bound=doc_count_error_upper_bound,
                                              sum_other_doc_count=sum_other_doc_count, buckets=buckets)
    return response_model
