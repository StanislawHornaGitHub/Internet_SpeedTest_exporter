from pydantic import BaseModel, Field, field_serializer, root_validator

from src.Model.SpeedTest.subModels.Ping import TransferPing

class Transfer(BaseModel):
    bandwidth: int = Field(default=0)
    bytes: int = Field(default=0)
    elapsed: int = Field(default=0)
    latency: TransferPing = Field(default=TransferPing())
    
    @field_serializer('bandwidth')
    def serialize_bandwidth(self, bandwidth: int, _info):
        return (bandwidth * 8)
    
    def __init__(self, **data):
        super().__init__(**data)
        self.bandwidth = self.bandwidth * 8