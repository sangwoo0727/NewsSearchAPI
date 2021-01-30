from typing import Optional, List
from datetime import date
from pydantic import BaseModel


class MatchDataModel(BaseModel):
    id: int
    score: float
    date: date
    category: str
    headline: str
    contents: str
