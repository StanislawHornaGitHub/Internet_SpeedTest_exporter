from pydantic import BaseModel, Field

from src.Model.SpeedTest.subModels.Ping import NoWorkloadPing
from src.Model.SpeedTest.subModels.Transfer import Transfer
from src.Model.SpeedTest.subModels.Interface import Interface
from src.Model.SpeedTest.subModels.Server import Server
from src.Model.SpeedTest.subModels.Result import Result


class SpeedTest(BaseModel):
    _type: str
    _timestamp: str
    ping: NoWorkloadPing
    download: Transfer
    upload: Transfer
    packet_loss: float = Field(alias='packetLoss')
    isp: str
    interface: Interface
    server: Server
    result: Result
