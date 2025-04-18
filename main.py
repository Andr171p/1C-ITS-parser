import json


file_path = r"C:\Users\andre\dio-1c-agent\parser\scraper\buh_results.json"

with open(file_path, encoding="utf-8") as file:
    data = json.load(file)

print(data[23]["page_text"])
