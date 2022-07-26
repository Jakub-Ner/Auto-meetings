import json
with open('s.json', "r+") as d:
    d = json.load(d)
    print(d)

    D = {"name":"Agatka"}
    d.update(D)
with open('s.json', "w+") as s:
    s.write(json.dumps(d))
