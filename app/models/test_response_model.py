from pydantic import BaseModel
from typing import Optional, List
from ..models.token_model import TokenModel


class TestResponseModel(BaseModel):
    total: int
    tokens: List[TokenModel]
