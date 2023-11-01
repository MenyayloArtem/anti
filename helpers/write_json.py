import json

def write_json(path, data):
    with open(f"{path}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=True, indent=4)