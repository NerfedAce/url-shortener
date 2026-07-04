from pydantic import BaseModel

class Url(BaseModel):
    short_url: str


class Entry(BaseModel):
    short_url: str
    long_url: str
    clicks: int
    region: str



