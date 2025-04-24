import json
import logging
import asyncio

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter  # , DomainFilter
from crawl4ai.deep_crawling.filters import ContentRelevanceFilter

from src.settings import BASE_DIR


async def main() -> None:
    # domain_filter = DomainFilter(allowed_domains=["https://v8.1c.ru/erp/"])
    filter_chain = FilterChain([URLPatternFilter(patterns=["*platforma*"])])
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=3, filter_chain=filter_chain),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://v8.1c.ru/platforma/", config=config)

        print(f"Crawled {len(results)} pages in total")

        file_path = BASE_DIR / "parsed_data" / "platform.json"
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                pages = []
                for result in results:
                    page = {
                        "url": result.url,
                        "content": result.markdown[3050:]
                    }
                    pages.append(page)
                data = json.dumps(pages, ensure_ascii=False)
                file.write(data)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
