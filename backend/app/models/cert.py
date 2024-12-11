from pydantic import BaseModel


class Cert(BaseModel):
    domain: str
