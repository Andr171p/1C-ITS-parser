from typing import List

import json
import requests
from lxml import html
from bs4 import BeautifulSoup
from html_to_markdown import convert_to_markdown


ALLOWED_DOMAINS = ["1c.ru", "v8.1c.ru"]
START_URL = "https://1c.ru/rus/products/1c/default.jsp"


def parse_links(html_content: str) -> List[str]:
    tree = html.fromstring(html_content)
    links = []
    links.extend(tree.xpath('//a/@href'))
    links.extend(tree.xpath('//link/@href'))
    links.extend(tree.xpath('//img/@src'))
    links.extend(tree.xpath('//script/@src'))
    links.extend(tree.xpath('//iframe/@src'))
    links.extend(tree.xpath('//meta[contains(@content, "url")]/@content'))
    return links


def filter_links(links: List[str]) -> List[str]:
    def check_link(link: str) -> bool:
        return True if "v8.1c.ru" in link and link != "http://v8.1c.ru/" else False
    return list(filter(check_link, links))


response = requests.get(START_URL)

html_content = response.text
soup = BeautifulSoup(html_content, "lxml")
found_links = parse_links(html_content)
filtered_links = filter_links(found_links)

products = []
for link in filtered_links:
    try:
        response = requests.get(link)
        print(f"Open {link}")
        soup = BeautifulSoup(response.text, "lxml")
        name = soup.find("h1", attrs={"class": "name"}).text.strip()
        text_block = soup.find("div", attrs={"class": "col-xl-7 offset-xl-1 col-lg-9 content"})
        description = convert_to_markdown(text_block)
        url_pattern = link.split("/")[3]
        product = {
            "url": link,
            "url_pattern": url_pattern,
            "name": name,
            "description": description
        }
        products.append(product)
    except Exception as ex:
        print(ex)

with open("../parsed_data/program_products.json", "w", encoding="utf-8") as file:
    data = json.dumps(products, ensure_ascii=False)
    file.write(data)
