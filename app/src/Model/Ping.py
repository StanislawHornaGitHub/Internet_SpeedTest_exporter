from pydantic import BaseModel

class Ping(BaseModel):
    jitter: float
    low: float
    high: float
    
class NoWorkloadPing(Ping):
    latency: float
    
class TransferPing(Ping):
    iqm: float