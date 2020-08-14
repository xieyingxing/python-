import json


def analyze(filename):
    with open("./data/" + filename + ".json", "r", encoding="utf-8") as f:
        dict_data = json.load(f)
        list_data = []
        for value in dict_data.values():
            list_data.append(value)
        return list_data