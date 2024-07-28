from pydantic import BaseModel, Field


class Interface(BaseModel):
    internal_ip: str = Field(alias='internalIp')
    name: str
    mac_address: str = Field(alias='macAddr')
    is_vpn: bool = Field(alias='isVpn')
    external_ip: str = Field(alias='externalIp')
