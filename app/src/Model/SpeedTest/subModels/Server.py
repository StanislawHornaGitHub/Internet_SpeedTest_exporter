from pydantic import BaseModel, field_serializer

class Server(BaseModel):
    id: int
    host: str
    port: int
    name: str
    location: str
    country: str
    ip: str
    
    @field_serializer('id')
    def serialize_id(self, id: int, _info):
        return str(id)
    
    @field_serializer('port')
    def serialize_port(self, port: int, _info):
        return str(port)