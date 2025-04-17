import re

from bs4 import BeautifulSoup

from langchain_community.document_loaders import RecursiveUrlLoader


def bs4_extractor(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    return re.sub(r"\n\n+", "\n\n", soup.text).strip()


loader = RecursiveUrlLoader("https://v8.1c.ru/lawmonitor/", extractor=bs4_extractor)
documents = loader.load()
print(documents)
print(len(documents))

text = ""
for document in documents:
    text += f"{document.page_content}\n\n"

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(text)
