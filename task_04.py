import json


with open("input.txt", "r", encoding='utf8') as f:
    data = json.load(f)
    processed_data = list(data.items())
    processed_data.sort(key=lambda x: x[1], reverse=True)
    print(processed_data)
