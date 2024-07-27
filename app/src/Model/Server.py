from pydantic import BaseModel

class Server(BaseModel):
    id: int
    host: str
    port: int
    name: str
    location: str
    country: str
    ip: str