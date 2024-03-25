import json

line = input()
data = json.loads(line)
processed_data = list(data.items())
processed_data.sort(key=lambda x: x[1], reverse=True)
print(processed_data)
