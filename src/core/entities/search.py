from pydantic import BaseModel


class SearchResult(BaseModel):
    url: str
    content: str
