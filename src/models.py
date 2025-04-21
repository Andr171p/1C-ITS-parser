from pydantic import BaseModel


class ProgramProduct(BaseModel):
    url: str
    url_pattern: str
    name: str
    description: str


class SearchResults(BaseModel):
    url: str
    content: str
