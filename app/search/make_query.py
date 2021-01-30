from helpers import load_json
from app.vector.vector_container import VectorContainer
import copy

vector_container = VectorContainer()


def get_match_all_query():
    origin_body = load_json("app/search/queries/match_all.json")
    body = copy.deepcopy(origin_body)
    return body


def get_match_query_basic(terms, analyzer, oper_flag=False):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        'must': [
            {
                'match': {
                    'contents': {
                        'query': terms,
                        'analyzer': analyzer
                    }
                }
            }
        ]
    }
    if oper_flag:
        body['query']['bool']['must'][0]['match']['contents']['operator'] = 'and'
    return body


def get_match_query_zero_terms(terms, analyzer, zero_terms_query=False):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        'must': [
            {
                'match': {
                    'contents': {
                        'query': terms,
                        'analyzer': analyzer
                    }
                }
            }
        ]
    }
    if zero_terms_query:
        body['query']['bool']['must'][0]['match']['contents']['zero_terms_query'] = 'all'
    return body


def get_multi_match_query(terms):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        'must': [
            {
                'multi_match': {
                    'query': terms,
                    'operator': 'and',
                    'fields': ['contents', 'headline']
                }
            }
        ]
    }
    return body


def get_match_phrase_basic(terms, slop):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        'must': [
            {
                'match_phrase': {
                    'contents': {
                        'query': terms
                    }
                }
            }
        ]
    }
    if slop > 0:
        body['query']['bool']['must'][0]['match_phrase']['contents']['slop'] = slop
    return body


def get_bool_must_match_query(must_first_terms, must_second_terms):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        'must': [
            {
                'match': {
                    'contents': {
                        'query': must_first_terms
                    }
                }
            },
            {
                'match': {
                    'contents': {
                        'query': must_second_terms
                    }
                }
            }
        ]
    }
    return body


def get_bool_match_query(must_terms, should_terms, filter_terms=None):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        'must': [
            {
                'match': {
                    'contents': {
                        'query': must_terms
                    }
                }
            }
        ],
        'should': [
            {
                'match': {
                    'contents': {
                        'query': should_terms
                    }
                }
            }
        ]
    }
    if filter_terms is not None:
        body['query']['bool']['filter'] = [{
            'term': {
                'contents': filter_terms
            }
        }]
    return body


def get_date_query(terms):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        'must': [
            {
                'match': {
                    'date': {
                        'query': terms
                    }
                }
            }
        ]
    }
    return body


def get_test_query(tokenizer, text):
    origin_body = load_json("app/search/queries/analyze_test.json")
    body = copy.deepcopy(origin_body)
    body['analyzer'] = tokenizer
    body['text'] = text
    return body


def get_multi_boost_query(boost, terms, boost_fields):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)

    f1 = 'contents'
    f2 = 'head_line'
    if f1 == boost_fields:
        f1 = f1 + '^' + boost
    if f2 == boost_fields:
        f2 = f2 + '^' + boost

    body['query']['bool'] = {
        'must': [
            {
                'multi_match': {
                    'query': terms,
                    'fields': [
                        f1, f2
                    ]
                }
            }
        ]
    }
    return body


def get_email_query(email):
    origin_body = load_json("app/search/queries/match.json")
    body = copy.deepcopy(origin_body)
    body['query']['bool'] = {
        "must": [
            {
                "match": {
                    "contents.email": email
                }
            }
        ]
    }
    return body


def get_highlight_query(terms):
    origin_body = load_json("app/search/queries/default_match.json")
    body = copy.deepcopy(origin_body)
    body['query']['match']['contents'] = terms
    body['highlight'] = {
        "fields": {
            "contents": {}
        }
    }
    return body


def get_highlight_query_with_size(terms, size):
    origin_body = load_json("app/search/queries/default_match.json")
    body = copy.deepcopy(origin_body)
    body['query']['match']['contents'] = terms
    body['highlight'] = {
        'fields': {
            'contents': {
                'fragment_size': size
            }
        }
    }
    return body


def get_highlight_query_with_max_size(terms, size):
    origin_body = load_json("app/search/queries/default_match.json")
    body = copy.deepcopy(origin_body)
    body['query']['match']['contents'] = terms
    body['highlight'] = {
        'fields': {
            'contents': {
                'number_of_fragments': size
            }
        }
    }
    return body


def get_highlight_query_with_tag(terms, tag):
    origin_body = load_json("app/search/queries/default_match.json")
    body = copy.deepcopy(origin_body)
    body['query']['match']['contents'] = terms
    body['highlight'] = {
        'fields': {
            'contents': {
                'pre_tags': ['<' + tag + '>'],
                'post_tags': ['</' + tag + '>']
            }
        }
    }
    return body


def get_search_with_sort_option(terms, option):
    origin_body = load_json("app/search/queries/default_match.json")
    body = copy.deepcopy(origin_body)
    body['query']['match']['product'] = terms
    body['sort'] = [
        {
            "price": {
                "order": "desc",
                "mode": option
            }
        }
    ]
    return body


def get_agg_query_basic(fields):
    origin_body = load_json("app/search/queries/agg.json")
    body = copy.deepcopy(origin_body)
    body['aggs'] = {
        'my-agg': {
            "terms": {
                "field": fields
            }
        }
    }
    return body


def get_vector_match_query(terms, query_vector):
    origin_body = load_json("app/search/queries/vector_match.json")
    body = copy.deepcopy(origin_body)

    body['query']['script_score']['query']['bool']['must']['match']['contents']['query'] = terms
    body['query']['script_score']['script']['source'] = vector_container.use_cosine_similarity_scoring()
    body['query']['script_score']['script']['params']['query_vector'] = query_vector
    return body


def get_vector_weight_match_query(terms, weight, query_vector):
    body = get_vector_match_query(terms, query_vector)
    body['query']['script_score']['script']['source'] = vector_container.use_cosine_similarity_scoring_weight(weight)
    body['query']['script_score']['script']['params']['weight'] = weight
    return body
