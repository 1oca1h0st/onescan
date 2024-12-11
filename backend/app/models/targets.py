from pydantic import BaseModel


class Targets(BaseModel):
    ips: str
