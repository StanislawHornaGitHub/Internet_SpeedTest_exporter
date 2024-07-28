from pydantic import BaseModel, field_serializer

class Result(BaseModel):
    id: str
    url: str
    persisted: bool
    
    @field_serializer('persisted')
    def serialize_persisted(self, persisted: int, _info):
        return str(persisted)