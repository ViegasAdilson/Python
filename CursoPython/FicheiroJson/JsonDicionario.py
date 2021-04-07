import json

d1 = {
    "Pessoas 1": {
        "nome": "Adilson",
        "idade": 35,
    },
    "Pessoas 2": {
        "nome": "Benvindo",
        "idade": 56,
    },
}

d1_json = json.dumps(d1, indent=True)
with open("abc.json", "w+") as file:
    file.write(d1_json)

