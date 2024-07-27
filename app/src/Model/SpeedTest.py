from pydantic import BaseModel

from src.Model.Ping import NoWorkloadPing
from src.Model.Transfer import Transfer
from src.Model.Interface import Interface
from src.Model.Server import Server
from src.Model.Result import Result

class SpeedTest(BaseModel):
    type: str
    timestamp: str
    ping: NoWorkloadPing
    download: Transfer
    upload: Transfer
    packetLoss: float
    isp: str
    interface: Interface
    server: Server
    result: Result
    