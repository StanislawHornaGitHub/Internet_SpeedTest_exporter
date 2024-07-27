from pydantic import BaseModel

from src.Model.Ping import TransferPing

class Transfer(BaseModel):
    bandwidth: int
    bytes: int
    elapsed: int
    latency: TransferPing
    