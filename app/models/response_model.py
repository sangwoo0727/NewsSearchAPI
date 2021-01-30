from typing import Optional, List
from pydantic import BaseModel
from app.models.match_data_model import MatchDataModel
from datetime import date


class ResponseModel(BaseModel):
    total: int
    max_score: float
    data: List[MatchDataModel]


class HighlightModel(BaseModel):
    id: int
    score: float
    date: date
    category: str
    headline: str
    contents: str
    highlight: List[str]


class HighlightResponseModel(BaseModel):
    total: int
    max_score: float
    data: List[HighlightModel]


class SortModeModel(BaseModel):
    product: str
    price: List[int]
    sort: List[int]


class SortModeResponseModel(BaseModel):
    data: List[SortModeModel]


class AggregationResponseModel(BaseModel):
    doc_count_error_upper_bound: int
    sum_other_doc_count: int
    buckets: list


class VectorModel(BaseModel):
    id: int
    score: float
    date: date
    category: str
    headline: str
    contents: str
