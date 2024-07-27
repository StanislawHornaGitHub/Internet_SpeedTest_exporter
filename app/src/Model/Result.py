from pydantic import BaseModel

class Result(BaseModel):
    id: str
    url: str
    persisted: bool