import ipaddress

from pydantic import BaseModel, Field, field_validator


# class for maxpatrol vm
class Host(BaseModel, validate_assignment=True):
    ip: str
    port: int = Field(ge=1, le=65535)
    username: str = Field(min_length=1)
    password: str = Field(min_length=0)
    os_name: str = ''
    os_ver: str = ''
    os_arch: str = ''

    @field_validator('ip')
    def check_ip(cls, ip: str) -> str:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            raise ValueError('invalid IP address')
        return ip
