from pydantic import BaseModel, Field

from src.Model.SpeedTest.subModels.Ping import NoWorkloadPing
from src.Model.SpeedTest.subModels.Transfer import Transfer
from src.Model.SpeedTest.subModels.Interface import Interface
from src.Model.SpeedTest.subModels.Server import Server
from src.Model.SpeedTest.subModels.Result import Result


class SpeedTest(BaseModel):
    _type: str
    _timestamp: str
    ping: NoWorkloadPing = Field(default=NoWorkloadPing())
    download: Transfer = Field(default=Transfer())
    upload: Transfer = Field(default=Transfer())
    packet_loss: float = Field(alias='packetLoss', default=0.0)
    isp: str = Field(default="-")
    interface: Interface = Field(default=Interface())
    server: Server = Field(default=Server())
    result: Result = Field(default=Result())
