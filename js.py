import json

with open('setting.json', 'r', encoding='utf-8') as file:
    data =json.load(file)
    print(data)

    a = "".join(str1.split())