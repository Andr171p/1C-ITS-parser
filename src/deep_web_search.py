from typing import List

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    ContentRelevanceFilter
)

from src.models import SearchResults


class DeepWebSearch:
    def __init__(
            self,
            url: str,
            max_depth: int = 1,
            threshold: float = 0.7
    ) -> None:
        self._url = url
        self._max_depth = max_depth
        self._threshold = threshold

    async def search(self, query: str) -> List[SearchResults]:
        relevance_filter = ContentRelevanceFilter(
            query=query,
            threshold=self._threshold
        )
        url_pattern_filter = URLPatternFilter(patterns=...)
        filter_chain = FilterChain([url_pattern_filter, relevance_filter])
        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=self._max_depth,
                filter_chain=filter_chain
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True
        )
        async with AsyncWebCrawler() as crawler:
            results = await crawler.arun(url=self._url, config=config)
        return [SearchResults(url=result.url, content=result.markdown) for result in results]

    async def allowed_url_patterns(self, query: str) -> List[str]:
        ...
