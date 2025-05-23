import json

def load_input(path: str) -> dict:
    with open(path, 'r') as f:
        return json.load(f)