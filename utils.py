import re
from bs4 import BeautifulSoup


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
