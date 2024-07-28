from pydantic import BaseModel, Field, field_serializer

from src.Model.SpeedTest.subModels.Ping import TransferPing

class Transfer(BaseModel):
    bandwidth: int = Field(default=0)
    bytes: int = Field(default=0)
    elapsed: int = Field(default=0)
    latency: TransferPing = Field(default=TransferPing())
    
    @field_serializer('bandwidth')
    def serialize_bandwidth(self, bandwidth: int, _info):
        return float((bandwidth / 10**6) * 8)