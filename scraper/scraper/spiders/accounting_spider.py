import re
from typing import Any
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import scrapy
from scrapy.http import Response


class AccountingSpider(scrapy.Spider):
    name = "accounting"
    start_urls = ["https://v8.1c.ru/buhv8/"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        all_text = ' '.join(response.css('body *::text').getall())
        cleaned_text = extract_clean_text(all_text)

        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'h1': response.css('h1::text').get(),
            'text': cleaned_text,
            'text_length': len(cleaned_text),
            'meta_description': response.css('meta[name="description"]::attr(content)').get(),
        }

        for link in response.css('a::attr(href)').getall():
            if self.should_follow_link(link, response.url):
                absolute_url = urljoin(response.url, link)
                yield scrapy.Request(absolute_url, callback=self.parse)

    @staticmethod
    def should_follow_link(link: str, base_url: str) -> bool:
        if link.startswith(('#', 'javascript:', 'mailto:', 'tel:')):
            return False
        if any(ext in link.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.jpg', '.png']):
            return False
        absolute_url = urljoin(base_url, link)
        return "https://v8.1c.ru/buhv8/" in absolute_url


def extract_clean_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    for element in soup(['script', 'style', 'noscript', 'iframe', 'form', 'button', 'input', 'select', 'textarea']):
        element.decompose()

    for tag in soup.find_all():
        for attr in list(tag.attrs):
            if attr.startswith(('on', 'data-')) or attr in {'href', 'src'}:
                del tag[attr]

    text = soup.get_text(separator='\n', strip=True)

    text = re.sub(r'javascript:\S+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\{.*?\}|\[.*?\]|\(.*?\)', '', text)
    text = re.sub(r'<\s*script[^>]*>.*?<\s*/\s*script\s*>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<\s*style[^>]*>.*?<\s*/\s*style\s*>', '', text, flags=re.DOTALL | re.IGNORECASE)

    text = re.sub(r'[\xa0\u200b\ufeff]', ' ', text)
    text = re.sub(r'\s*\n\s*', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)

    text = re.sub(r'(?<!\w)[^\w\s](?!\w)', '', text)

    return text.strip()
