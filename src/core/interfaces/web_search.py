from typing import List
from abc import ABC, abstractmethod

from src.core.entities import SearchResult


class AbstractWebSearch(ABC):
    @abstractmethod
    async def search(self, query: str) -> List[SearchResult]:
        raise NotImplemented
