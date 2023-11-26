import json


def task() -> float:
    with open("input.json", 'r') as f:
        data = json.load(f)
        values = [item["score"] * item["weight"] for item in data]
    return round(sum(values), 3)


print(task())