from pydantic import BaseModel, field_serializer

from src.Model.SpeedTest.subModels.Ping import TransferPing

class Transfer(BaseModel):
    bandwidth: int
    bytes: int
    elapsed: int
    latency: TransferPing
    
    @field_serializer('bandwidth')
    def serialize_bandwidth(self, bandwidth: int, _info):
        return float((bandwidth / 10**6) * 8)