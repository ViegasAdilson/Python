import json

with open("abc.json", "r") as file:
    d1_json = file.read()
    novo_d1 = json.loads(d1_json)


for k, p in novo_d1.items():
    print(k)
    for n, i in p.items():
        print(n, i)