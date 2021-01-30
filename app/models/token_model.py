from pydantic import BaseModel


class TokenModel(BaseModel):
    token: str
    start_offset: int
    end_offset: int
    position: int
