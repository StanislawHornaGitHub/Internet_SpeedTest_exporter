from pydantic import BaseModel, Field


class Interface(BaseModel):
    internal_ip: str = Field(alias='internalIp', default="-")
    name: str = Field(default="-")
    mac_address: str = Field(alias='macAddr', default="-")
    is_vpn: bool = Field(alias='isVpn', default="-")
    external_ip: str = Field(alias='externalIp', default="-")
