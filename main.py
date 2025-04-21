import json

file_path = r"C:\Users\andre\dio-1c-agent\parser\parsed_data\answer.json"


with open(file_path, "r", encoding="utf-8") as file:
    data = json.loads(file.read())


print(len(data))

print(data[2])

